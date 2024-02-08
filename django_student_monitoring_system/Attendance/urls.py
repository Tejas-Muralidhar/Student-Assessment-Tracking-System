from django.urls import path
from .views import attendance_entry_view,show_attendance_view

urlpatterns = [
    path('attendance-entry/', attendance_entry_view, name='attendance_entry'),
    path('attendance-view/', show_attendance_view, name="attendance_view"),
]
