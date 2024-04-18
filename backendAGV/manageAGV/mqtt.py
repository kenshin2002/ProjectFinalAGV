import paho.mqtt.client as mqtt
from django.conf import settings
import json
import math
import time







def on_connect(mqtt_client, userdata, flags, rc):
   if rc == 0:
       print('Connected MQTT successfully')
       mqtt_client.subscribe('58kpuw3237/dataespsend')
       mqtt_client.subscribe('58kpuw3237/datawebsend')
   else:
       print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    from manageAGV.models import AGV_data
    try:
        # Chuyển đổi dữ liệu JSON thành đối tượng Python
        data = json.loads(msg.payload)
        
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
    

#Connection to the client is established here
client = mqtt.Client() #instantiating the mqtt client.
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)

