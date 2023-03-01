from django.contrib import admin
from storage.models import UrlStorage, UrlBunchStorage, HtmlStorage, HtmlBunchStorage


admin.site.register(UrlStorage)
admin.site.register(UrlBunchStorage)
admin.site.register(HtmlStorage)
admin.site.register(HtmlBunchStorage)
