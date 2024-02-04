from django.shortcuts import render
from django.http import JsonResponse

def student_profile_view(request): #Accessed by Student, Fac and HOD
    '''
    Implement student profile logic here
    show student deets like usn phone sem etc etc. //Faculty and Hod
    SPstudent_profile(IN usn) 
    it gets back table having USN, Name, Sem, Phone, Parent_Phone, Subject_Code, Subject_Name 
    '''
    return JsonResponse({'message': 'Student profile view'})

def student_mapping_view(request): #Accessed by Student, Fac and HOD
    '''
    Implement subject enrollment logic here
    student subject and mark and attendance. 
    SPstudent_mapping(IN usn)
    it gets back table of everything related to student. Personal details, Marks, Attendance and Faculty Name of every subject taken.
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

#views to write down to send info into db like faculty entering marks