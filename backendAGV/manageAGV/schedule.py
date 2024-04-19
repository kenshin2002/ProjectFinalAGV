from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from datetime import datetime
global_counter = 0

# jobs
def FirstCronTest():
    global global_counter
    global_counter += 1
    print("I am executed..!", global_counter)
def startShe():
   scheduler = BackgroundScheduler()
   scheduler.add_job(FirstCronTest, 'interval', seconds=30)
   scheduler.start()