from django.shortcuts import render
from django.http import JsonResponse

def subject_list_view(request):
    # Implement subject list logic here
    return JsonResponse({'message': 'Subject list view'})

def subject_details_view(request, subject_id):
    # Implement subject details logic here
    return JsonResponse({'message': f'Subject details view for subject {subject_id}'})

