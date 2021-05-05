from django.conf.urls import url
from django.urls import path
from djangostuffs.coins import views

urlpatterns = [
    path('', views.get_coin),
]