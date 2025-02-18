from .service import storage


def job():
    storage.delete_old_keys()


def start():
    from apscheduler.schedulers.background import BlockingScheduler
    from django_apscheduler.jobstores import DjangoJobStore, register_events
    sch = BlockingScheduler()
    sch.add_jobstore(DjangoJobStore(), "default")

    sch.add_job(
        job,
        trigger='interval',
        hours=1,
        id="my_job",
        max_instances=1,
        replace_existing=True,
    )

    sch.start()