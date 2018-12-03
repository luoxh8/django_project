from apscheduler.schedulers.background import BackgroundScheduler

APS_SCHEDULER_CONFIG = {
    'jobstores'   : {
        'default': {'type': 'sqlalchemy', 'url': 'sqlite:///job.sqlite3'},
    },
    'executors'   : {
        'default': {'type': 'processpool', 'max_workers': 10}
    },
    'job_defaults': {
        'coalesce'          : True,
        'max_instances'     : 5,
        'misfire_grace_time': 30
    },
    'timezone'    : 'Asia/Shanghai'
}


class Scheduler:
    _scheduler = BackgroundScheduler()
    _scheduler.configure(APS_SCHEDULER_CONFIG)
    _is_start = False

    def start_work(self):
        if not self._is_start:
            self._is_start = True
            self._scheduler.start()

    def stop_work(self):
        if self._is_start:
            self._is_start = False
            self._scheduler.shutdown()

    def add_job(self, func, time, job_name):
        self._scheduler.add_job(func, trigger='interval', seconds=time, id=job_name)
        self._scheduler.print_jobs()

    def re_add_job(self, func, time, job_name):
        self._scheduler.reschedule_job(job_name, trigger="interval", seconds=time)
        self._scheduler.print_jobs()

    def remove_job(self, job_name):
        self._scheduler.remove_job(job_name)
        self._scheduler.print_jobs()


scheduler = Scheduler()
scheduler.start_work()

"""
{"id":"1","route":"heartbeat","req_data":""}
"""
