from django.db import models

class AGV(models.Model):
    GUIDANCE_TYPE = (
        ('OPT', 'Optical Tape'),
        ('MAG', 'Magnetic Tape'),
        ('WIR', 'Wire Guided'),
        ('LZR', 'Laser Guided')
    )
    LOAD_TRANSFER = (
        ('AUTO', 'Automatic'),
        ('MAN', 'Manual')
    )
    vehicle_id = models.BigAutoField(primary_key=True, blank=False)
    vehicle_model = models.CharField(max_length=255, blank=True)  # Sửa đổi thành CharField
    maximum_battery = models.IntegerField(default=0)
    maximum_velocity = models.IntegerField(default=0)
    guidance_type = models.CharField(max_length=255, blank=True, choices=GUIDANCE_TYPE)
    loading_type = models.CharField(max_length=255, choices=LOAD_TRANSFER)
    is_active = models.BooleanField(default=True)
    is_connected = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}. Is active: {self.is_active}"

class AGV_data(models.Model):
    data_id = models.BigAutoField(primary_key=True)
    car_id = models.IntegerField()
    carSpeed = models.IntegerField()
    previousNode = models.IntegerField()
    nextNode = models.IntegerField()
    carBattery = models.IntegerField()
    carState = models.IntegerField()
    carObstac = models.IntegerField(default=0)
   

class AGVStates(models.Model):
    state_id = models.BigAutoField(primary_key=True)
    carState = models.BooleanField(default=False)
    
class DataSchedule(models.Model):
    schedule_id=models.BigAutoField(primary_key=True)
    order_date=models.DateTimeField(blank= True)
    order_number_id=models.IntegerField()
    load_name=models.CharField(max_length=255,default='Metal')
    load_weight=models.IntegerField(default=25)
    car_id=models.IntegerField()
    est_start_time=models.TimeField(blank= True)
    est_end_time=models.TimeField(blank= True)
    begin_node=models.IntegerField()
    destination_node=models.IntegerField()
    est_distance=models.IntegerField()
    est_energy=models.IntegerField(default=0)
    is_complete=models.BooleanField(default=False)
class orderData(models.Model):
    request_id=models.BigAutoField(primary_key=True)
    orderDate=models.DateTimeField(blank=True)
    orderNumber=models.IntegerField(default=0)
    loadName=models.CharField(max_length=255,default='Metal')
    load_weight=models.IntegerField(default=25)
    start_time=models.CharField(max_length=255,default='00:00')
    startPoint=models.IntegerField(default=0)
    endPoint=models.IntegerField(default=0)
class DB_StationData(models.Model):
    STATION_TYPE = (
        ('HOME', 'Parking station'),
        ('BAT', 'Charging station'),
        ('PICK', 'Pick up'),
        ('DROP', 'Drop') 
        # TO ADD MORE CUZ I CANT THINK OF ANYTHING RN
    )
    LOAD_TRANSFER = (
        ('AUTO', 'Automatic'),
        ('MAN', 'Manual')
    )
    
    station_id = models.IntegerField(primary_key= True, blank= False)
    station_node = models.IntegerField(default= 0)
    station_type = models.CharField(max_length=64, blank=True, choices= STATION_TYPE)
    load_transfer = models.CharField(max_length=64, blank=True, choices= LOAD_TRANSFER)
    is_active = models.BooleanField(default= False)

    def __str__(self):
        return "Station ID: {ID}".format(ID = self.station_id)
