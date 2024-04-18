from django.shortcuts import render
from django.utils import timezone
from time import sleep

from .models import AGV_data,AGV

def is_agv_active(topic):
    carID = topic.split("/") 
    AGVisActive = AGV.objects.all().filter(vehicle_id = carID[1], is_active = True).exists()
    return AGVisActive

def list_active_AGV():
    listOfActiveAGV = []
    AGVisActive = AGV.objects.all().filter(is_active = True)
    for eachQuery in AGVisActive:
        listOfActiveAGV.append(eachQuery.vehicle_id)
    listOfActiveAGV.sort()

    return listOfActiveAGV

