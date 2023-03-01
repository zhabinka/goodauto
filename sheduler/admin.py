from django.contrib import admin
from sheduler.models import CrawlerFrontier, ParserFrontier


admin.site.register(CrawlerFrontier)
admin.site.register(ParserFrontier)
