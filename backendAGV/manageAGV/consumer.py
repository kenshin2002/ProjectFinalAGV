from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.core import serializers
from .activeAGV import list_active_AGV
from .models import AGV_data
from time import sleep

@database_sync_to_async
def jsonize_active_agv():
    queryList = []
    listOfAGV = []
    listOfAGV = list_active_AGV()
    for eachCar in listOfAGV:
        query = AGV_data.objects.filter(car_id = eachCar).last()
        if query:
            queryList.append(query)
        else:
            pass

    queryFields = ('car_id', 'carState', 'carBattery', 'carSpeed', 'previousNode')
    jsonSet = serializers.serialize('json', queryset=queryList, fields = queryFields)

    return jsonSet

class AsyncJsonConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            jsonSet = await jsonize_active_agv()
            await self.send(jsonSet)
            sleep(0.2)

    async def disconnect(self):
        pass
