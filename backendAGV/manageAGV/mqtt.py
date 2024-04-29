import paho.mqtt.client as mqtt
from django.conf import settings
import json
import math
import time
from datetime import datetime
from django.utils import timezone
from . import DjikStraAlgo
DjikStraAlgo.initialize_map()
def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected MQTT successfully')
        mqtt_client.subscribe('58kpuw3237/dataespsend')
        mqtt_client.subscribe('58kpuw3237/dataschedule')
        # Đăng ký các chủ đề MQTT khác nếu cần
    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    if msg.topic == '58kpuw3237/dataespsend':
        handle_data_from_espsend(msg.payload)
    elif msg.topic == '58kpuw3237/dataschedule':
        handle_websend_topic(msg.payload)
    
def handle_data_from_espsend(payload):
    from manageAGV.models import AGV_data
    try:
        # Chuyển đổi dữ liệu JSON thành đối tượng Python
        data = json.loads(payload)
        
        # Tạo một đối tượng AGV_data mới từ dữ liệu JSON
        agv_data = AGV_data(
            data_id=4,
            car_id=data['car_id'],
            carSpeed=data['carSpeed'],
            previousNode=data['previousNode'],
            nextNode=data['nextNode'],
            carBattery=data['carBattery'],
            carState=data['carState'],
            carObstac=data.get('carObstac', 0)  # Dùng get để tránh lỗi nếu 'carObstac' không có trong JSON
        )
        
        # Lưu đối tượng AGV_data vào cơ sở dữ liệu
        agv_data.save()
        
        print('Data saved successfully to the database.')
    except Exception as e:
        print('Error processing message:', e)

def handle_websend_topic(payload):
 
    from manageAGV.models import orderData
    try:
        # Chuyển đổi dữ liệu JSON thành đối tượng Python
        data = json.loads(payload)
        current_time = timezone.now()
        current_time_rounded = current_time.replace(microsecond=0)
        # Tạo một đối tượng orderData mới từ dữ liệu JSON
        new_order = orderData(
            
            orderDate=current_time_rounded,
            orderNumber=data.get('id'),
            loadName=data.get('load_name', 'Metal'),  
            load_weight=float(data.get('load_weight', 25)),  
            start_time=data.get('start_time', '00:00'), 
            startPoint=data.get('start_point', 0),  
            endPoint=data.get('end_point', 0)  
        )
        
        # Lưu đối tượng orderData vào cơ sở dữ liệu
        new_order.save()
        startPoint=int(data.get('start_point', 0)) 
        endPoint=int(data.get('end_point', 0))
        shortest_path=DjikStraAlgo.dijkstra(startPoint,endPoint)
        route_string = DjikStraAlgo.create_route(shortest_path,DjikStraAlgo.directions)
        print("Route:", route_string)
        data_to_publish = {
         "AGV": "1",
        "path": route_string  # Đường đã được tạo trước đó
         }

         # Chuyển đổi dữ liệu JSON thành chuỗi
        json_string = json.dumps(data_to_publish)
        
        # Publish dữ liệu lên MQTT
        client.publish('58kpuw3237/databackend', json_string)
        print('Data saved successfully to the database.')
    except Exception as e:
        print('Error processing message:', e)



client = mqtt.Client() #instantiating the mqtt client.
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
client.loop_start()


    