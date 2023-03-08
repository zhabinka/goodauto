import datetime
import os

from django_cron import CronJobBase, Schedule
from sheduler.crawler import scrapy_bunches
from sheduler.parser import parse_bunches

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
CRAWLER_LOG_FILE = os.path.join(CUR_DIR, '../logs/cron/crawler.txt')
PARSER_LOG_FILE = os.path.join(CUR_DIR, '../logs/cron/parser.txt')


class RunUrlBunchCrawler(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlBunchCrawler'

    def do(self):
        limit = 1
        scrapy_bunches(limit=limit)
        message = f'{datetime.datetime.now()} Downloaded {limit} bunch(es) \n'
        with open(CRAWLER_LOG_FILE, "a") as f:
            f.write(message)


class RunUrlBunchParser(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlBunchParser'

    def do(self):
        parse_bunches()
        message = f'{datetime.datetime.now()} All bunches processed \n'
        with open(PARSER_LOG_FILE, "a") as f:
            f.write(message)
