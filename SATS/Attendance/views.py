import json
from django.shortcuts import render,redirect
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
                    return render(request,'DataDisplay.html',{'display': 'attendance','data': attendance_data, 'view': 'Student'})
                    
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
            # Decode the request body
            data = json.loads(request.body)
            print(data)

            # Assuming data is a list of lists
            headers = data[0]  # Extract headers from the first row
            result = []

            # Iterate over each row starting from the second row
            for row in data[1:]:
                # Create a dictionary for the current row
                row_dict = {}
                for i, header in enumerate(headers):
                    # Assign data to the corresponding header key in the dictionary
                    row_dict[header] = row[i]
                # Append the dictionary to the result list
                result.append(row_dict)

            # Now, result contains a list of dictionaries where each dictionary represents a row of data
            print(result)
            # Iterate over the rows starting from the second row (index 1)
            for row in result:
                print(row)
                # Extract data from each row
                usn = row.get('USN')
                print(usn)
                subject_code = row.get('SubjectCode')
                sem = row.get('Sem')
                section = row.get('Section')
                attended = row.get('Attended')
                maxclasses = row.get('MaxClasses')
                percentage = row.get('Percentage')

                # Convert data to JSON string
                json_data = json.dumps({
                    "usn": usn,
                    "subjectCode": subject_code,
                    "semester": sem,
                    "section": section,
                    "attended": attended,
                    "maxclasses": maxclasses,
                    "percentage": percentage
                })
                print(json_data)
                # Call the stored procedure with the JSON data
                with connection.cursor() as cursor:
                    cursor.callproc('SPInsertStudentAttendance', [json_data]) #also call SPInsertMaxAttendance and sedn appropriate data to update both.
            return JsonResponse({'message': 'Student marks inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
