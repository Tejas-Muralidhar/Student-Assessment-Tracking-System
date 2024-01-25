from django.urls import path
from .views import mark_entry_view,mark_list_view

urlpatterns = [
    path('view-marks/',mark_list_view,name='marks-view'),
    path('edit-marks/',mark_entry_view,name='marks-edit'),
]
