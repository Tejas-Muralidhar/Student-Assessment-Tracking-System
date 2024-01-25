from django.urls import path
from .views import user_login_view,user_profile_view,user_registration_view

urlpatterns = [
    path('register-user/',user_registration_view,name='user-registration'),
    path('user-login/',user_login_view,name='user-login'),
    path('view-user-profile/',user_profile_view,name='view-profile'),

]
