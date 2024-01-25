from django.urls import path
from .views import faculty_profile_view,faculty_subject_assignment_view

urlpatterns = [
    path('view-faculty-profile/',faculty_profile_view,name='faculty-profile'),
    path('faculty-mapping/',faculty_subject_assignment_view,name='faculty-subject-mapping'),
]
