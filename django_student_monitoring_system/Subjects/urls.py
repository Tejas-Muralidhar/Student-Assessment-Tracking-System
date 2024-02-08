from django.urls import path
from .views import subject_details_view

urlpatterns = [
    path('details-subject/<str:subject_id>/',subject_details_view,name='subject-details'),
]
