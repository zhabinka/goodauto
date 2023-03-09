import datetime
import os

from django_cron import CronJobBase, Schedule
from sheduler.crawler import scrapy_bunches, add_crawler_tasks, scrapy
from sheduler.parser import parse_bunches, add_parser_tasks, parse

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
CRAWLER_LOG_FILE = os.path.join(CUR_DIR, '../logs/cron/crawler.txt')
PARSER_LOG_FILE = os.path.join(CUR_DIR, '../logs/cron/parser.txt')


class RunUrlBunchCrawler(CronJobBase):
    RUN_EVERY_MINS = 10
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlBunchCrawler'

    def do(self):
        limit = 1
        scrapy_bunches(limit=limit)
        message = f'[BUNCH] {datetime.datetime.now()} Downloaded {limit} bunch(es) \n'
        with open(CRAWLER_LOG_FILE, "a") as f:
            f.write(message)


class RunUrlCrawler(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlCrawler'

    def do(self):
        limit = 2
        scrapy(limit=limit)
        message = f'[URL] {datetime.datetime.now()} Downloaded {limit} url(s) \n'
        with open(CRAWLER_LOG_FILE, "a") as f:
            f.write(message)


class RunUrlParser(CronJobBase):
    RUN_EVERY_MINS = 2
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlParser'

    def do(self):
        parse()
        message = f'{datetime.datetime.now()} All urls processed \n'
        with open(PARSER_LOG_FILE, "a") as f:
            f.write(message)


class RunUrlBunchParser(CronJobBase):
    RUN_EVERY_MINS = 2
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.RunUrlBunchParser'

    def do(self):
        parse_bunches()
        message = f'{datetime.datetime.now()} All bunches processed \n'
        with open(PARSER_LOG_FILE, "a") as f:
            f.write(message)


class AddShedulerTasks(CronJobBase):
    RUN_EVERY_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.AddShedulerTasks'

    def do(self):
        add_crawler_tasks()
        add_parser_tasks()
        message = f'{datetime.datetime.now()} Add tasks to sheduler \n'
        with open(PARSER_LOG_FILE, "a") as f:
            f.write(message)
