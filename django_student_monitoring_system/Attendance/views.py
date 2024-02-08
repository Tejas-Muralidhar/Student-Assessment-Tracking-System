from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pandas as pd  # Import pandas library for working with Excel files
from django.db import connection

def show_attendance_view(request):
    # Implement attendance list logic here
    return JsonResponse({'message': 'Attendance list view'})


@csrf_exempt
def attendance_entry_view(request): #path is localhost:8000/attendance/attendance-entry/
    if request.method == 'POST':
        try:
            # Check if the request contains a file
            if 'file' not in request.FILES:
                return JsonResponse({'error': 'No file uploaded'}, status=400)
            
            # Get the uploaded Excel file
            excel_file = request.FILES['file']
            
            # Read the Excel file using pandas
            df = pd.read_excel(excel_file)
            
            # Loop through each row in the DataFrame
            for index, row in df.iterrows():
                # Extract attendance details from each row
                usn = row['USN']
                fid = row['FID']
                subject_code = row['SubjectCode']
                attended = row['Attended']
                max_classes = row['MaxClasses']
                
                # Call the stored procedure with extracted values
                with connection.cursor() as cursor:
                    cursor.callproc('SPInsertAttendance', [usn, fid, subject_code, attended, max_classes])
                    
                    # Commit the transaction
                    connection.commit()
            
            return JsonResponse({'message': 'Attendance inserted successfully'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)