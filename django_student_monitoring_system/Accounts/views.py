from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse

@csrf_exempt  # Disable CSRF protection for simplicity; consider enabling in production
def user_registration_view(request):
    # Implement user registration logic here
    # You may use Django forms for user registration
    return JsonResponse({'message': 'User registration view'})

@csrf_exempt
def user_login_view(request):
    # Implement user login logic here
    # You may use Django forms for user login
    return JsonResponse({'message': 'User login view'})

def user_profile_view(request):
    # Implement user profile logic here
    return JsonResponse({'message': 'User profile view'})

