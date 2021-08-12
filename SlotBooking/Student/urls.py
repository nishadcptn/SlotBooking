from django.contrib import admin
from django.urls import path
from Student.views import *

urlpatterns = [
    path('student/', StudentApi.as_view(), name='studentApi'),
    path('student/<int:pk>', StudentApi.as_view(), name='studentApi'),
]