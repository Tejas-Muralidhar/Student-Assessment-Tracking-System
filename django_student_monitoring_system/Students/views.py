from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def MapStudentSubject(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            ip_user_type_key = data_json.get('user_type_key')
            ip_subject_code = data_json.get('subject_code')

            with connection.cursor() as cursor:
                cursor.callproc('SPMapStudentSubject', [ip_user_type_key, ip_subject_code])
                return JsonResponse({'message': 'Student subject mapping successful'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)