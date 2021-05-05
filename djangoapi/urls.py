from django.conf.urls import url
from django.urls import path
from .views import CoinView

urlpatterns = [
    path('coin', CoinView.as_view())
]