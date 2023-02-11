# import time
# import re
#
# from bs4 import BeautifulSoup
#
# from django.db import transaction
#
# from sheduler.driver import init_chrome_webdriver
# from sheduler.models import CrawlFrontier, ParserFrontier
# from storage.models import HtmlStorage, UrlStorage
# from goodauto.cars.models import Car
# from goodauto.cars.views import set_task_to_parse_car
# from storage import url
#
#
# def set_crawl_task(url_):
#     item = url.to_storage(url_)
#     if item:
#         id = CrawlFrontier.objects.create(external_url_id=item)
#         print(f'Add {item.external_url} in sheduler')
#         return id
#
#
# def scrapy():
#     driver = init_chrome_webdriver()
#     tasks = CrawlFrontier.objects.all()
#
#     try:
#         for task in tasks[:10]:
#             url = task.external_url_id.external_url
#             driver.get(url=url)
#             time.sleep(2)
#
#             item, _ = HtmlStorage.objects.get_or_create(
#                 external_url_id=task.external_url_id
#             )
#             item.source_html = driver.page_source
#             item.save()
#
#             # add to parse frontier
#             set_task_to_parse_car(item)
#
#             print(f'[INFO] Downloaded html from {url}')
#
#             url_storage = UrlStorage.objects.get(external_url=url)
#             url_storage.processed = True
#
#             with transaction.atomic():
#                 task.delete()
#                 url_storage.save()
#                 print(f'[INFO] Removed {url} from sheduler')
#
#     except Exception as e:
#         print(f'[ERROR] {e}')
#     finally:
#         driver.close()
#         driver.quit()
#
#     print(f'[INFO] All tasks complited')
#
#
# def parse():
#     tasks = ParserFrontier.objects.all()
#     for task in tasks:
#         html = task.source_html_id.source_html
#         page = BeautifulSoup(html, 'lxml')
#         price = page.select('div[class*=PriceWrapper]')[0].find('div')
#         title = page.find('h1')
#
#         item = task.car_id
#         item.price = int(re.sub('[^0-9]', '', price.text))
#         item.name = title.text
#         item.external_url_id = task.source_html_id.external_url_id
#         print(item)
#         print(price)
#         print(title)
#         print(task.source_html_id.external_url_id)
#         item.save()
#
#         html_storage = HtmlStorage.objects.get(source_html=html)
#         html_storage.processed = True
#
#         with transaction.atomic():
#             task.delete()
#             html_storage.save()
#             print(f'[SUCCESS] Added car {title}')
#             print(f'[] Removed task')
#
#     print(f'[INFO] All task complited')
