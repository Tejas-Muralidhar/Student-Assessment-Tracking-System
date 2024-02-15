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
            # data_json={
            #     'userTypeKey' :'FAC002',
            #     'subjectCode':'21CS31',
            #     'section':'C'
            # }
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