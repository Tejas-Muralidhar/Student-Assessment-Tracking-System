from django.urls import path
from .views import AllMarksSubject,GetSubjects,InsertSubjects

urlpatterns = [
    path('show-subject-marks/',AllMarksSubject,name='AllMarksSubject'), #admin use
    path('get-subjects/',GetSubjects,name="GetSubjects"), #faculty and student use
    path('insert-subjects/',InsertSubjects,name="InsertSubjects"),
]
