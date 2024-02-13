from django.shortcuts import render
# from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.http import HttpResponse

from goodauto.cars.models import Car, UrlStorage


def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)


def to_storage(html_storage):
    item, _ = Car.objects.get_or_create(
        html_storage=html_storage,
        url_storage=html_storage.url_storage,
        car_model=html_storage.url_storage.car_model
    )
    return item


class CarDetail(DetailView):
    model = Car
    template_name = 'cars/detail.html'


def remove_closed_car_urls():
    removed_car_ids = []
    for car in Car.objects.filter(closed=True):
        url = UrlStorage.objects.get(id=car.url_storage.id)
        model = '{} {}'.format(car.car_model.brand, car.car_model.model)
        id = car.id
        url.delete()
        removed_car_ids.append((model, id))
        print(f'[SUCCES] Car {model} ({id}) has removed')
    return removed_car_ids


def test(request):
    # request.headers['Host'] = '100.0.0.0:8080'
    context = {
        'meta': request.META,
        'headers': request.headers,
    }
    return render(request, 'cars/headers.html', context)
    # return HttpResponse('hello ' + request.get_host() +
    #                     ' ' + request.method +
    #                     ' ' + str(request.COOKIES) +
    #                     ' ' + str(request.content_params) +
    #                     ' ' + str(request.META) +
    #                     ' ' + str(request.headers))
