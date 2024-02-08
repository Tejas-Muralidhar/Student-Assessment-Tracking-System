from django.shortcuts import render
from django.http import JsonResponse

def marks_entry_view(request):
    # Implement mark entry logic here
    return JsonResponse({'message': 'Mark entry view'})

def show_marks_view(request): #usn and that students all marks #subject code and show all students marks studying that subject
    # Implement mark list logic here
    return JsonResponse({'message': 'Mark list view'})

