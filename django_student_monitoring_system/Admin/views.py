from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def AdmFacMapSub(request):
    data = {}
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
                data['message'] = f'Mapped Faculty {ipUserTypeKey} to Subject {ipSubjectCode} successfully!'
                return render(request,'Admin.html',data)
            except Exception as e:
                # Handle exceptions appropriately
                data['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return redirect('Login')
        
def AdmViewFaculty(request):
    response = {}
    if request.method == "GET":
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
                response['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',response)
    else:
        response['message'] = f'Illegal Action!'
        return render(request,'Admin.html',response)
        
def AdmViewStudentAttendance(request):
    response = {}
    if request.method == "GET":
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
                response['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',response)
    else:
        response['message'] = f'Illegal Action!'
        return render(request,'Admin.html',response)
        
def AdmViewStudentMarks(request):
    response = {}
    if request.method == "GET":
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
                response['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',response)
    else:
        response['message'] = f'Illegal Action!'
        return render(request,'Admin.html',response)
        
def AdmViewStudents(request):
    data = {}
    if request.method == "GET":
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
                data['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return render(request,'Admin.html',data)
            
@csrf_exempt
def AdmDeleteSubject(request):
    data = {}
    if request.method == "POST":
        sCodeDel = request.POST.get('subject_code')
        with connection.cursor() as cursor:
            try:
                # Call the stored procedure
                cursor.callproc('ADMSubDelete', [sCodeDel])
                results = cursor.fetchall()                    
                data['message'] = f'Deletion of the Subject {sCodeDel} was successful!'
                return render(request,'Admin.html',data)
            except Exception as e:
                data['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return render(request,'Admin.html',data)


def AdmViewSubjects(request):
    response = {}
    if request.method == "GET":
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
                response['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',response)
    else:
        response['message'] = f'Illegal Action!'
        return render(request,'Admin.html',response)
        
@csrf_exempt        
def AdmDeleteUser(request):
    data = {}
    if request.method == "POST":
        del_value = request.POST.get('user_input')
        with connection.cursor() as cursor:
            try:
                cursor.callproc('ADMUserDel', [del_value])
                results = cursor.fetchall()
                data['message'] = f'Deletion of the User ID {del_value} was successful!'
                return render(request,'Admin.html',data)
            except Exception as e:
                data['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return render(request,'Admin.html',data)

@csrf_exempt        
def AdmViewUsers(request):
    data={}
    if request.method == "GET":
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
                data['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return render(request,'Admin.html',data)
        
@csrf_exempt
def AdmAddEditSubject(request):
    data={}
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
                data['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',data)
        
        data['message'] = f'Addition/Updation of Subject {subject_code} was successful!'
        return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return render(request,'Admin.html',data)

@csrf_exempt
def ADMFacViewMapping(request):
    response ={}
    if request.method == 'GET':
        with connection.cursor() as cursor:
            try:
                cursor.callproc('ADMFacViewMapping')
                results = cursor.fetchall()
                # Convert results to a list of dictionaries
                print(results)
                data = []
                for row in results:
                    data.append({
                        'Faculty ID': row[0],
                        'Faculty Name': row[1],
                        'Subject Code': row[2],
                        'Subject Title': row[3],
                        'Semester': row[4],
                        'Section': row[5],
                        # Add more columns as needed
                    })
                return JsonResponse({'data': data})
            except Exception as e:
                response['message'] = f'Something went wrong! {str(e)}'
                return render(request,'Admin.html',response)
    else:
        response['message'] = f'Illegal Action!'
        return render(request,'Admin.html',response)
    
@csrf_exempt
def ADMUserAddEdit(request):
    data={}
    if request.method == 'POST':
        try:
            user_type = request.POST.get('user_type')

            if user_type == 'Student':

                usn = request.POST.get('USN')
                name = request.POST.get('Name')
                gender = request.POST.get('Gender')
                dateOfBirth = request.POST.get('DOB')
                parentNumber = request.POST.get('ParentNumber')
                userEmail = request.POST.get('Email')
                userPassword = request.POST.get('Password')
                Phone = request.POST.get('Phone')
                Semester = request.POST.get('Semester')
                Section = request.POST.get('Section')

                user_key = usn

                json_data = json.dumps({
                "usn": usn,
                "name":name,
                "gender":gender,
                "dateOfBirth":dateOfBirth,
                "parentNumber":parentNumber,
                "userEmail":userEmail,
                "userPassword":userPassword,
                "Phone":Phone,
                "roleId_id":1
                })

            else:

                facultyID = request.POST.get('FID')
                facultyName = request.POST.get('Name')
                gender = request.POST.get('Gender')
                userEmail = request.POST.get('Email')
                userPassword = request.POST.get('Password')
                Phone = request.POST.get('Phone')

                user_key = facultyID

                json_data = json.dumps({
                "facultyID": facultyID,
                "facultyName":facultyName,
                "gender":gender,
                "userEmail":userEmail,
                "userPassword":userPassword,
                "Phone":Phone,
                "roleId_id": 2
                })

            # Call the stored procedure with the JSON data
            with connection.cursor() as cursor:
                cursor.callproc('ADMUserCreateEdit', [user_type,json_data])
                results = cursor.fetchall()

            if user_type == 'Student':
                json_data1 =  json.dumps({
                    "Usn": usn,
                    "Sem": Semester,
                    "Section": Section
                })
                print(json_data1)
                with connection.cursor() as cursor:
                    cursor.callproc('ADMUserMapStuSem',[json_data1])
                    results = cursor.fetchall()
                
            data['message'] = f'Addition/Updation of {user_type} {user_key} was successful!'
            return render(request,'Admin.html',data)
        
        except Exception as e:
            data['message'] = f'Something went wrong! {str(e)}'
            return render(request,'Admin.html',data)
    else:
        data['message'] = f'Illegal Action!'
        return render(request,'Admin.html',data)