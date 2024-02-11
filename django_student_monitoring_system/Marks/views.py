from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.http import HttpResponse
from openpyxl import Workbook

def InsertStudentMarks(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            with connection.cursor() as cursor:
                cursor.callproc('SPInsertStudentMarks', [data])
                return JsonResponse({'message': 'Student marks inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
    

def GetStudentMarksWithMax(request):
    if request.method == 'GET':
        user_type_key = request.GET.get('user_type_key')  # Assuming user_type_key is passed as a query parameter
        
        try:
            with connection.cursor() as cursor:
                cursor.callproc('SPGetStudentMarksWithMax', [user_type_key]) #takes in only USN! 
                columns = [col[0] for col in cursor.description]
                
                # Fetch the row for the user
                rows = cursor.fetchall()
                
                if rows:
                    # Convert row to dictionary
                    marks_data = [dict(zip(columns, row))for row in rows]

                    # ~~~~~~~~~~~~
                    wb = Workbook()
                    ws = wb.active

                    # Write header row
                    headers = list(marks_data[0].keys())
                    ws.append(headers)

                    for row in marks_data:
                        ws.append([row.get(column, '') for column in headers])

                    # Create a response with the Excel content type
                    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    response['Content-Disposition'] = 'attachment; filename=my_excel_file.xlsx'

                    # Save the workbook to the response
                    wb.save(response)

                    return response

                    # return JsonResponse({'marks_data': marks_data})
                else:
                    return JsonResponse({'message': 'Marks data not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

