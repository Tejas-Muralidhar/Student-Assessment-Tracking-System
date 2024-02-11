from django.urls import path
from .views import say_goodbye

urlpatterns =[
    path('abcd/',say_goodbye)
]