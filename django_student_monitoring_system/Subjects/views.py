from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from Accounts.views import UserAuthorization 

def AllMarksSubject(request):
    if request.method == 'GET':
        subject_code = request.GET.get('subject_code')  # Assuming subject_code is passed as a query parameter
        
        try:
            with connection.cursor() as cursor:
                cursor.callproc('SPAllMarksSubject', [subject_code])
                columns = [col[0] for col in cursor.description]
                
                # Fetch the rows for the subject
                rows = cursor.fetchall() #found inconsistency in tables called by procedure
                
                if rows:
                    # Convert rows to list of dictionaries
                    marks_data = [dict(zip(columns, row)) for row in rows]
                    return JsonResponse({'number of tuples':len(rows),'marks_data': marks_data})
                else:
                    return JsonResponse({'message': 'Marks data not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    
@csrf_exempt
def GetSubjects(request):
    if request.method == 'GET':
        user_type_key = request.GET.get('user_type_key')  # Assuming usn or facid is passed as a query parameter
        
        with connection.cursor() as cursor:
            cursor.callproc('SPGetSubjects', [user_type_key])
            res = cursor.fetchall()
            # Fetch the result set returned by the stored procedure
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in res]

            # Return the results as JSON response
            return render(request,'DataDisplay.html',{'display':'subjects','data': results})
    else:
        # Return error response for non-GET requests
        data = {'message': 'Only GET requests are allowed'}
        return render(request,'ErrorPage.html',data)

@csrf_exempt
def InsertSubjects(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            # data_json = {
            # "subjectCode": "21CS21",
            # "subjectName": "Math2",
            # "subjectType": 1,
            # "sem": 2,
            # "isElective": 0,
            # "credits": 3,
            # "IA1": 50,
            # "IA2": 50,
            # "IA3": 50,
            # "avgIA": 50,
            # "assignment1": 10,
            # "assignment2": 10,
            # "quiz1": 10,
            # "quiz2": 10,
            # "maxIAMarks": 50,
            # "labObservation": 0,
            # "labRecord": 0,
            # "labViva": 0,
            # "maxEAMarks":50
            # }

            with connection.cursor() as cursor:
                cursor.callproc('SPInsertSubjects', [json.dumps(data_json)])
                return JsonResponse({'message': 'Subjects inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        data = {'message': 'Only POST requests are allowed', 'status':405}
        return render(request,'ErrorPage.html',data)