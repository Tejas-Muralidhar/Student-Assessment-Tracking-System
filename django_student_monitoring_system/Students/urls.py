from django.urls import path
from .views import student_profile_view,student_mapping_view

urlpatterns = [
    path('view-student-profile/',student_profile_view,name='student-profile'),
    path('student-mapping/',student_mapping_view,name='student-subject'),
]
