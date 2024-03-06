from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def AdmFacMapSub(request):
    if request.method == "POST":
        ipUserTypeKey = request.POST.get('faculty_id')
        ipSubjectCode = request.POST.get('subject_code')
        ipSection = request.POST.get('section')
        ipSem = request.POST.get('semester')

        with connection.cursor() as cursor:
            try:
                cursor.callproc('ADMFacMapSub', [ipUserTypeKey, ipSubjectCode, ipSection, ipSem])
                # If the procedure has any output parameters, you can fetch them like this:
                # output_data = cursor.fetchone()
                # You can use JsonResponse to return any data if needed.
                return JsonResponse({'message': 'Stored procedure executed successfully'})
            except Exception as e:
                # Handle exceptions appropriately
                return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Only POST requests allowed!'})
        
def AdmViewFaculty(request):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMFacViewFaculty')
            results = cursor.fetchall()
            # Convert results into a list of dictionaries for JSON serialization
            faculty_list = []
            for row in results:
                faculty_dict = {
                    'Faculty ID': row[0],
                    'Faculty Name': row[1],
                    'Gender': row[2],
                    'Email': row[3],
                    'Phone': row[4],
                }
                faculty_list.append(faculty_dict)
            return JsonResponse({'faculty': faculty_list})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
def AdmViewStudentAttendance(request):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMStuViewAtt')
            results = cursor.fetchall()
            # Convert results into a list of dictionaries for JSON serialization
            attendance_list = []
            for row in results:
                attendance_dict = {
                    'USN': row[0],
                    'Semester': row[1],
                    'Section': row[2],
                    'Subject Code': row[3],
                    'Classes Attended': row[4],
                    'Total Classes': row[5],
                    'Percentage': row[6]
                    # Add more fields as needed
                }
                attendance_list.append(attendance_dict)
            return JsonResponse({'attendance': attendance_list})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
def AdmViewStudentMarks(request):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMStuViewMarks')
            results = cursor.fetchall()
            # Convert results into a list of dictionaries for JSON serialization
            marks_list = []
            labmarks_list = []
            for row in results:
                if row[0] == 1:
                    marks_dict = {
                        'USN' : row[1],
                        'Subject Code': row[2],
                        'IA 1':row[3],
                        'IA 2':row[4],
                        'IA 3':row[5],
                        'Assignment 1':row[7],
                        'Assignment 2':row[8],
                        'Quiz 1':row[9],
                        'Quiz 2':row[10],
                        'Average IA': row[6],
                        'Final IA': row[14],
                        'Final EA': row[15],
                        # Add more fields as needed
                    }
                    marks_list.append(marks_dict)
                else:
                    labmarks_dict = {
                        'USN' : row[1],
                        'Subject Code': row[2],
                        'IA 1':row[3],
                        'IA 2':row[4],
                        'IA 3':row[5],
                        'Record':row[11],
                        'Observation':row[12],
                        'Viva':row[13],
                        'Average IA': row[6],
                        'Final IA': row[14],
                        'Final EA': row[15],
                        # Add more fields as needed
                    }
                    labmarks_list.append(labmarks_dict)
            data = {
                'theorymarks': marks_list,
                'labmarks': labmarks_list
            }
            return JsonResponse({'marks': data})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
def AdmViewStudents(request):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMStuViewStudents')
            results = cursor.fetchall()
            # Convert results into a list of dictionaries for JSON serialization
            students_list = []
            for row in results:
                student_dict = {
                    'USN': row[0],
                    'Name': row[1],
                    'Gender': row[2],
                    'Date Of Birth': row[3],
                    'Email': row[4],
                    'Phone': row[5],
                    'Parent/Guardian Contact': row[7]
                    # Add more fields as needed
                }
                students_list.append(student_dict)
            return JsonResponse({'students': students_list})
        except Exception as e:
            return JsonResponse({'error': str(e)})
            
@csrf_exempt
def AdmDeleteSubject(request):
    if request.method == "POST":
        sCodeDel = request.POST.get('subject_code')
        with connection.cursor() as cursor:
            try:
                # Call the stored procedure
                cursor.callproc('ADMSubDelete', [sCodeDel])
                results = cursor.fetchall()                    
                return JsonResponse({'message': 'Subject deleted successfully'})
            except Exception as e:
                return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Only POST Requests are allowed'})


def AdmViewSubjects(request):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMSubViewDetails')
            results = cursor.fetchall()
            # Convert results into a list of dictionaries for JSON serialization
            subjects_list = []
            labsubjects_list=[]
            for row in results:
                if row[2] == 1:
                    subject_dict = {
                        'Subject Code': row[0],
                        'Subject Title': row[1],
                        'Semester': row[3],
                        'Credits': row[5],
                        'Max IA Marks': row[6],
                        'Max Quiz Marks': row[12],
                        'Max Assignment Marks': row[10],
                        'Average IA Marks': row[9],
                        'Max Internal Marks': row[17],
                        'Max External Marks': row[18]
                        # Add more fields as needed
                    }
                    subjects_list.append(subject_dict)
                else:
                    labsubject_dict = {
                        'Subject Code': row[0],
                        'Subject Title': row[1],
                        'Semester': row[3],
                        'Credits': row[5],
                        'Max IA Marks': row[6],
                        'Max Record Marks': row[15],
                        'Max Observation Marks': row[14],
                        'Max Viva Marks': row[16],
                        'Average IA Marks': row[9],
                        'Max Internal Marks': row[17],
                        'Max External Marks': row[18]
                        # Add more fields as needed
                    }
                    labsubjects_list.append(labsubject_dict)
            data = {
                'theorymarks': subjects_list,
                'labmarks': labsubjects_list
            }
            return JsonResponse({'marks': data})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
def AdmDeleteUser(request):
    del_value = request.GET.get('user_type_key')

    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMUserDel', [del_value])
            return JsonResponse({'message': 'User deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
def AdmViewUsers(request):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('ADMUserView')
            results = cursor.fetchall()
            # Convert results into a list of dictionaries for JSON serialization
            users_list = []
            for row in results:
                user_dict = {
                    'User ID': row[6],
                    'User Email': row[2],
                    'User Type': row[5],
                    'Logged in': row[4],
                    # Add more fields as needed
                }
                users_list.append(user_dict)
            return JsonResponse({'users': users_list})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
@csrf_exempt
def AdmAddEditSubject(request):
    if request.method == 'POST':
        # Retrieve data from the form POST request
        subject_code = request.POST.get('subject_code')
        subject_name = request.POST.get('subject_name')
        semester = request.POST.get('semester')
        subject_type = request.POST.get('lab_or_theory')
        is_elective = 0
        credits = request.POST.get('credits')
        ia1 = request.POST.get('MaxIA')
        ia2 = request.POST.get('MaxIA')
        ia3 = request.POST.get('MaxIA')
        assignment1 = request.POST.get('MaxAssignment') 
        assignment2 = request.POST.get('MaxAssignment') 
        quiz1 = request.POST.get('MaxQuiz') 
        quiz2 = request.POST.get('MaxQuiz')
        lab_observation = request.POST.get('MaxObservation') 
        lab_record = request.POST.get('MaxRecord')
        lab_viva = request.POST.get('MaxViva')
        max_IA_marks = request.POST.get('MaxInternals')
        max_EA_marks = request.POST.get('MaxExternals')

        # Convert data to JSON string
        json_data = json.dumps({
            "subjectCode": subject_code,
            "subjectName": subject_name,
            "subjectType": subject_type,
            "sem": semester,
            "credits": credits,
            "isElective" : is_elective,
            "IA1": ia1,
            "IA2": ia2,
            "IA3": ia3,
            "avgIA": (int(ia1) + int(ia2) + int(ia3)) / 3,
            "assignment1": assignment1,
            "assignment2": assignment2,
            "quiz1": quiz1,
            "quiz2": quiz2,
            "labObservation": lab_observation,
            "labRecord": lab_record,
            "labViva": lab_viva,
            "maxIAMarks": max_IA_marks,
            "maxEAMarks": max_EA_marks
        })
        
        with connection.cursor() as cursor:
            try:
                cursor.callproc('ADMSubAddEditSub', [json_data])
            except Exception as e:
                return JsonResponse({'error': str(e)})
        
        return JsonResponse({"message": "Data submitted successfully."})

    else:
        return JsonResponse({"error": "Only POST requests are allowed."})