from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from datetime import datetime
global_startTime = 0
global_startPoint=0
global_endPoint=0
def FirstCronTest(start_time, start_point, end_point):
    global global_startTime, global_startPoint, global_endPoint
    global_startTime = start_time
    global_startPoint= start_point
    global_endPoint=end_point
    print("Công việc được thực hiện vào thời điểm:", start_time)
    print("Điểm bắt đầu:", start_point)
    print("Điểm kết thúc:", end_point)

def startScheduler(start_time, start_point, end_point):
    scheduler = BackgroundScheduler()
    scheduler.add_job(FirstCronTest, 'interval', seconds=30, args=[start_time, start_point, end_point])
    scheduler.start()

if __name__ == "__main__":
     pass
