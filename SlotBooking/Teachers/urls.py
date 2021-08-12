from django.contrib import admin
from django.urls import path,include
from Teachers.views import *

urlpatterns = [
    path('teacher/', TeacherApi.as_view(), name='TeacherApi'),
    path('teacher/<int:pk>', TeacherApi.as_view(), name='TeacherApi'),
    path('teacher/punchin/', AttandanceApi.as_view(), name='punchin'),
    path('teacher/punchout/', Punchout.as_view(), name='punchout'),
    path('slots/', SlotsApi.as_view(), name='SlotsControll'),
    path('teacher/show-availability/', AvailableSlots.as_view(), name='show-availability'),
    path('teacher/book/', BookingApi.as_view(), name='SlotBooking'),

]