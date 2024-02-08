from django.urls import path
from .views import user_authentication,user_profile_view,insert_user_details

urlpatterns = [
    path('register-user/',insert_user_details,name='user-registration'),
    path('user-auth/',user_authentication,name='user-auth'),
    path('view-profile/',user_profile_view,name='view-profile'),

]
