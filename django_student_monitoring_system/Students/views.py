from django.shortcuts import render
from django.http import JsonResponse

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

# from django.http import JsonResponse
# from django.db import connection

# def get_subjects(request):
#     if request.method == 'GET':
#         user_id = request.GET.get('user_id')  # Assuming user_id is passed as a query parameter
        
#         with connection.cursor() as cursor:
#             cursor.callproc('SPGetSubjects', [user_id])
#             # Fetch the result set returned by the stored procedure
#             cursor.execute('SELECT * FROM #TEMPORARY_TABLE_NAME')  # Replace #TEMPORARY_TABLE_NAME with the actual name of the temporary table created in your stored procedure
#             columns = [col[0] for col in cursor.description]
#             results = [dict(zip(columns, row)) for row in cursor.fetchall()]

#             # Return the results as JSON response
#             return JsonResponse({'subjects': results})
#     else:
#         # Return error response for non-GET requests
#         return JsonResponse({'message': 'Only GET requests are allowed'})