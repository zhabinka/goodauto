from django.views.generic.base import TemplateView
from django.urls import path
from goodauto.cars import views


app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.CarDetail.as_view(), name='detail'),
    # path('', views.IndexView.as_view())
    path('test', views.test)
]
