from django.shortcuts import render
from django.http import JsonResponse

def subject_details_view(request, subject_id): #Student, Hod and Faculty only!
    '''
    Implement code to get details from tables and send it back if it is Hod or faculty.
    SPsubject_details_view(IN semester) and gives back table of details regarding that semester's subjects (Cname, Ccode, credit)
    '''
    return JsonResponse({'message': f'Subject details view for subject {subject_id}'})

