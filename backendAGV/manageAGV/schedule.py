from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz

def FirstCronTest(start_time, start_point, end_point):
    print("Công việc được thực hiện vào thời điểm:", start_time)
    print("Điểm bắt đầu:", start_point)
    print("Điểm kết thúc:", end_point)

def startScheduler(start_time_str, start_point, end_point):
    # Chuyển chuỗi thời gian thành đối tượng datetime
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    # Đặt múi giờ cho thời gian bắt đầu
    start_time = pytz.timezone('Asia/Ho_Chi_Minh').localize(start_time)
    
    scheduler = BackgroundScheduler()
    # Sử dụng cron để lên lịch công việc
    scheduler.add_job(FirstCronTest, 'cron', args=[start_time, start_point, end_point], year=start_time.year, month=start_time.month, day=start_time.day, hour=start_time.hour, minute=start_time.minute, second=start_time.second)
    scheduler.start()

if __name__ == "__main__":
    # Test lên lịch khi chạy trực tiếp từ tệp script
    pass
