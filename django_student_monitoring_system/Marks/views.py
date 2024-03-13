import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from django.http import HttpResponse
from openpyxl import Workbook
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def InsertStudentMarks(request):
    if request.method == 'POST':
        print("Hello")
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
                ia1_score = row.get('IA1Score')
                ia2_score = row.get('IA2Score')
                ia3_score = row.get('IA3Score')
                quiz1_score = row.get('Quiz1Score')
                quiz2_score = row.get('Quiz2Score')
                assignment1_score = row.get('Assignment1Score')
                assignment2_score = row.get('Assignment2Score')
                labrecord_score = row.get('LabRecordScore')
                labviva_score = row.get('LabVivaScore')
                labobservation_score = row.get('LabObservationScore')

                # Convert data to JSON string
                json_data = json.dumps({
                    "usn": usn,
                    "subjectCode": subject_code,
                    "IA1Score": ia1_score,
                    "IA2Score": ia2_score,
                    "IA3Score": ia3_score,
                    "Quiz1Score": quiz1_score,
                    "Quiz2Score": quiz2_score,
                    "Assignment1Score": assignment1_score,
                    "Assignment2Score": assignment2_score,
                    "labRecordMarks": labrecord_score,
                    "labObservationMarks": labobservation_score,
                    "labVivaMarks": labviva_score
                })
                print(json_data)
                # Call the stored procedure with the JSON data
                with connection.cursor() as cursor:
                    print("Going to SP")
                    cursor.callproc('SPInsertStudentMarks', [json_data])
                    print("Came back from SP")
                print("Last line of loop")
            return JsonResponse({'message': 'Student marks inserted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



def DownloadStudentMarksWithMax(request):
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
        data = {'message': 'Only GET requests are allowed', 'status':405}
        return render(request,'ErrorPage.html',data)

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def GetStudentMarksWithMax(request):
    if request.method == 'GET':
        print("Hello")
        user_type_key = request.GET.get('user_type_key')  # Assuming user_type_key is passed as a query parameter
        with connection.cursor() as cursor:
            cursor.callproc('SPGetLogValue',[user_type_key])
            result = cursor.fetchone()
        print(result[0])
        if result[0]:
            try:
                with connection.cursor() as cursor:
                    # Call SPGetStudentMarksWithMax
                    cursor.callproc('SPGetStudentMarksWithMax', [user_type_key])
                    columns = [col[0] for col in cursor.description]
                    rows = cursor.fetchall()
                    # Convert row to dictionary
                    marks_data = [dict(zip(columns, row)) for row in rows]
                    for data in marks_data:
                        for key, value in data.items():
                            if value is None:
                                data[key] = '-'  # Replace None with '-'
                    # Call SPGetLabMarksWithMax
                with connection.cursor() as cursor:
                    cursor.callproc('SPGetLabMarksWithMax', [user_type_key])
                    columns = [col[0] for col in cursor.description]
                    rows = cursor.fetchall()
                    # Convert row to dictionary
                    lab_marks_data = [dict(zip(columns, row)) for row in rows]
                    for data in lab_marks_data:
                        for key, value in data.items():
                            if value is None:
                                data[key] = '-'  # Replace None with '-'
                return render(request, 'DataDisplay.html', {'display': 'marks', 'data': marks_data, 'lab_data': lab_marks_data, 'view': 'Student'})
                    
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return redirect('Login')
    else:
        data = {'message': 'Only GET requests are allowed', 'status':405}
        return render(request, 'ErrorPage.html', data)
