from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

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

def GetSubjects(request):
    if request.method == 'GET':
        user_type_key = request.GET.get('user_type_key')  # Assuming usn or facid is passed as a query parameter
        
        with connection.cursor() as cursor:
            cursor.callproc('SPGetSubjects', [user_type_key])
            # Fetch the result set returned by the stored procedure
            cursor.execute('SELECT * FROM #TEMPORARY_TABLE_NAME')  # Replace #TEMPORARY_TABLE_NAME with the actual name of the temporary table created in your stored procedure
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

            # Return the results as JSON response
            return JsonResponse({'subjects': results})
    else:
        # Return error response for non-GET requests
        return JsonResponse({'message': 'Only GET requests are allowed'})