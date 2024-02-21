from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pandas as pd  # Import pandas library for working with Excel files
from django.db import connection

def GetAttendance(request):
    if request.method == 'GET':
        user_type_key = request.GET.get('user_type_key')  # Assuming user_type_key is passed as a query parameter
        
        try:
            with connection.cursor() as cursor:
                cursor.callproc('SPGetAttendance', [user_type_key]) #only USN as of now
                columns = [col[0] for col in cursor.description]
                
                # Fetch the rows for the user
                rows = cursor.fetchall()
                
                if rows:
                    # Convert rows to list of dictionaries
                    attendance_data = [dict(zip(columns, row)) for row in rows]
                    return render(request,'DataDisplay.html',{'display': 'attendance','data': attendance_data })
                    
                else:
                    data = {'message': 'Attendance Data not found!', 'status':404}
                    return render(request, 'ErrorPage.html', data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)    

@csrf_exempt
def InsertStudentAttendance(request): #to be changed in mysql SP
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            with connection.cursor() as cursor:
                cursor.callproc('SPInsertStudentAttendance', [data])
                return JsonResponse({'message': 'Student attendance data inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def InsertMaxAttendance(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            with connection.cursor() as cursor:
                cursor.callproc('SPInsertMaxAttendance', [data])
                return JsonResponse({'message': 'Maximum attendance data inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)