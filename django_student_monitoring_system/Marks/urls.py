from django.urls import path
from .views import marks_entry_view,show_marks_view

urlpatterns = [
    path('view-marks/',show_marks_view,name='marks-view'),
    path('edit-marks/',marks_entry_view,name='marks-edit'),
]
