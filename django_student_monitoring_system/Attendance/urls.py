from django.urls import path
from .views import InsertStudentAttendance,GetAttendance,InsertMaxAttendance

urlpatterns = [
    path('attendance-entry/', InsertStudentAttendance, name='InsertStudentAttendance'), #faculty use
    path('attendance-view/', GetAttendance, name="GetAttendance"), #student and faculty use
    path('set-max-attendance/',InsertMaxAttendance,name="InsertMaxAttendance") #faculty only
]
