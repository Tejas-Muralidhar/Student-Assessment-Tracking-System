from django.shortcuts import render
from django.http import JsonResponse

def student_profile_view(request):
    # Implement student profile logic here
    return JsonResponse({'message': 'Student profile view'})

def student_mapping_view(request):
    # Implement subject enrollment logic here
    return JsonResponse({'message': 'Subject enrollment view'})
