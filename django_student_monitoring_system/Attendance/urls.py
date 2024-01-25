from django.urls import path
from .views import attendance_entry_view,attendance_list_view

urlpatterns = [
    path('attendance-entry/', attendance_entry_view, name='attendance_entry'),
    path('attendance-view/', attendance_entry_view, name="attendance_view"),
]
