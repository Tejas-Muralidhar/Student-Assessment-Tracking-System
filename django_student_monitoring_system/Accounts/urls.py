from django.urls import path
from .views import UserAuthorization,UserProfile,InsertUserDetails,Login

urlpatterns = [
    path('register-user/',InsertUserDetails,name='InsertUserDetails'),
    path('user-auth/',UserAuthorization,name='UserAuthorization'),
    path('view-profile/',UserProfile,name='UserProfile'),
    path('',Login,name="Login"),
]
