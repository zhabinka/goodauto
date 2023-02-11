from django.shortcuts import render
# from django.contrib.auth import get_user_model
# from django.views.generic import ListView

from goodauto.cars.models import Car


def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)


def to_storage(html_storage):
    item, _ = Car.objects.get_or_create(
        html_storage=html_storage,
        url_storage=html_storage.url_storage,
    )
    return item
