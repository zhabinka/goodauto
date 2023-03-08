import datetime
import os

from django_cron import CronJobBase, Schedule
from sheduler.crawler import scrapy_bunches

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_FILE = os.path.join(CUR_DIR, '../logs/cron/test.txt')
CRAWLER_LOG_FILE = os.path.join(CUR_DIR, '../logs/cron/crawler.txt')


class RunUrlBunchCrawler(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlBunchCrawler'

    def do(self):
        scrapy_bunches(limit=1)
        message = f"{datetime.datetime.now()} Downloaded 1 bunch"
        with open(CRAWLER_LOG_FILE, "a") as f:
            f.write(message)

class WriteDateToFileCronJob(CronJobBase):
    """
    Write current date to file.
    """

    # schedule = Schedule(run_at_times=["12:20", "12:25"], retry_after_failure_mins=1)
    RUN_EVERY_MINS = 60
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.WriteDateToFileCronJob'

    def do(self):
        message = f"Current date: {datetime.datetime.now()} \n"
        with open(LOG_FILE, "a") as f:
            f.write(message)
