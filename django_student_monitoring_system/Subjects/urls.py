from django.urls import path
from .views import subject_details_view,subject_list_view

urlpatterns = [
    path('list-subjects/',subject_list_view,name='list-subjects'),
    path('details-subject/<str:subject_id>/',subject_details_view,name='subject-details'),
]
