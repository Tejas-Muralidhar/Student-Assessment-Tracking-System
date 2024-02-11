from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def student_mapping_view(request): #Accessed by Student, Fac and HOD
    '''
    Implement subject enrollment logic here
    student subject and mark and attendance. 
    SPstudent_mapping(IN usn)
    it gets back table of everything related to student. Personal details, Marks, Attendance of every subject taken.
    '''
    return JsonResponse({'message': 'Subject enrollment view'})

def multiple_student_mapping_view(request): #Accessed only by Faculty and Hod!
    '''
    Implement subject enrollment logic here
    student subject and mark and attendance.
    SPmultiple_student_mapping(IN semester, IN section)
    it gets back table of everything related to class of students. Personal details, Marks, Attendance and Faculty Name of every subject taken.
    '''
    return JsonResponse({'message':'This gives back multiple student subject mapping'})

# views to write down to send info into db like faculty entering marks

