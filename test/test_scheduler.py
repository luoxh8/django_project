# coding:utf-8
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
scheduler.add_job(func=aps_test, args=('一次性任务',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3)

scheduler.start()
