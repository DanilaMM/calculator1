from django.contrib import admin
from django.urls import path, include
from .views import Calculator

app_name = 'calculate'

urlpatterns = [
    path('', Calculator.as_view(), name='calculator'),
]