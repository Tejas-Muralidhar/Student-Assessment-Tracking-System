from django.urls import path
from .views import faculty_subject_view

urlpatterns = [
    path('faculty-mapping/',faculty_subject_view,name='faculty-subject-mapping'),
]
