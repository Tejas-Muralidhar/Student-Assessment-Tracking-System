from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt


def GetMyStudents(request):
    if request.method == 'GET':
        try:
            ip_faculty_id = request.GET.get('faculty_id')
            with connection.cursor() as cursor:
                cursor.callproc('SPGetMyStudents', [ip_faculty_id])
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
                students_data = [dict(zip(columns, row)) for row in rows]
                return JsonResponse({'students_data': students_data}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

@csrf_exempt
def MapFacultySubject(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            user_type_key = data_json.get('userTypeKey')
            subject_code = data_json.get('subjectCode')
            section = data_json.get('section')

            with connection.cursor() as cursor:
                cursor.callproc('SPMapFacultySubject', [user_type_key, subject_code, section])
                return JsonResponse({'message': 'Faculty subject mapping successful'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
@csrf_exempt
def get_student_marks(request):
    try:
        user_type_key = request.GET.get('user_type_key')
        # Call GetSubjects to get all subjects taught by the faculty
        with connection.cursor() as cursor:
            cursor.callproc('SPGetSubjects', [user_type_key])
            columns = [col[0] for col in cursor.description]
            subjects = cursor.fetchall()
            subjects_data = [dict(zip(columns, subject)) for subject in subjects]

            print(subjects_data)

        # Initialize empty lists to store marks and attendance
        marks_data = []
        labmarks_data = []

        for subject in subjects_data:
            subject_code = subject['SubjectCode']
            # Call GetSubjectMarks
            with connection.cursor() as cursor:
                cursor.callproc('SPGetTheorySubjectMarks', [subject_code])
                columns = [col[0] for col in cursor.description]
                marks = cursor.fetchall()
                marks_data.extend(marks)
            #call SPGetLabSubjectMarks call the data as lab_marks
        Marksdata = [dict(zip(columns, row)) for row in marks_data]
        for data in Marksdata:
            for key, value in data.items():
                if value is None:
                    data[key] = '-'  # Replace None with '-'
        #do the same for lab marks, REMOVE NULL
        return render(request,'DataDisplay.html',{'display': 'marks','data': Marksdata, 'view': 'Faculty'}) #send lab_marks also
    
    except Exception as e:
        data = {'message': e, 'status':500}
        return render(request, 'ErrorPage.html', data)
    
@csrf_exempt
def get_student_attendance(request):
    try:
        user_type_key = request.GET.get('user_type_key')
        # Call GetSubjects to get all subjects taught by the faculty
        with connection.cursor() as cursor:
            cursor.callproc('SPGetSubjects', [user_type_key])
            columns = [col[0] for col in cursor.description]
            subjects = cursor.fetchall()
            subjects_data = [dict(zip(columns, subject)) for subject in subjects]

        # Initialize empty lists to store marks and attendance
        attendance_data = []

        # Iterate over each subject and call GetSubjectMarks and GetSubjectAttendance
        # Iterate over each subject and call GetSubjectMarks and GetSubjectAttendance
        for subject in subjects_data:
            subject_code = subject['SubjectCode']
            # Call GetSubjectAttendance
            with connection.cursor() as cursor:
                cursor.callproc('SPGetSubjectAttendance', [subject_code])
                attendance = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                print(columns)
                attendance_data.extend(attendance)
        Attdata = [dict(zip(columns, row)) for row in attendance_data]
        print(Attdata)
        for data in Attdata:
            for key, value in data.items():
                if value is None:
                    data[key] = '-'  # Replace None with '-'
        return render(request,'DataDisplay.html',{'display': 'attendance','data': Attdata, 'view': 'Faculty'})
    
    except Exception as e:
        data = {'message': 'Something went wrong. Try again!!', 'status':500}
        return render(request, 'ErrorPage.html', data)