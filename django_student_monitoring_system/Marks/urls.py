from django.urls import path
from .views import InsertStudentMarks,GetStudentMarksWithMax

urlpatterns = [
    path('view-marks/',GetStudentMarksWithMax,name='GetStudentMarksWithMax'), #student use only
    path('edit-marks/',InsertStudentMarks,name='InsertStudentMarks'), #faculty only
]
