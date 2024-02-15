from django.urls import path
from .views import MapStudentSubject

urlpatterns = [
    path('map-student-subject/',MapStudentSubject,name='MapStudentSubject'),
]
