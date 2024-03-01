from django.urls import path
from .views import GetMyStudents,MapFacultySubject,get_student_attendance,get_student_marks

urlpatterns = [
    path('get-students/',GetMyStudents,name='GetMyStudents'),
    path('map-facutly-subject/',MapFacultySubject,name='MapFacultySubject'),
    path('get_student_attendance/',get_student_attendance,name='get_student_attendance'),
    path('get_student_marks/',get_student_marks,name='get_student_marks'),
]
