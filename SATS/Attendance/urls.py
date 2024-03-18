from django.urls import path
from .views import InsertStudentAttendance,GetAttendance

urlpatterns = [
    path('attendance-entry/', InsertStudentAttendance, name='InsertStudentAttendance'), #faculty use
    path('attendance-view/', GetAttendance, name="GetAttendance"), #student and faculty use
]
