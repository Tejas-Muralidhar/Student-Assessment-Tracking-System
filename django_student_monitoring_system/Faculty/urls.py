from django.urls import path
from .views import GetMyStudents,MapFacultySubject

urlpatterns = [
    path('get-students/',GetMyStudents,name='GetMyStudents'),
    path('map-facutly-subject/',MapFacultySubject,name='MapFacultySubject'),
]
