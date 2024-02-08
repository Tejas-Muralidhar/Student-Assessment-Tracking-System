from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.db import connection

@csrf_exempt
def user_profile_view(request): #path is: localhost:8000/accounts/view-profile/
    if request.method == 'GET':
        userTypeKey = request.GET.get('userTypeKey')  # Assuming user_id is passed as a query parameter
        
        try:
            with connection.cursor() as cursor:
                cursor.callproc('SPUserProfile', [userTypeKey])
                columns = [col[0] for col in cursor.description]
                
                # Fetch the row for the user
                row = cursor.fetchone()
                
                if row:
                    # Convert row to dictionary
                    profile_data = dict(zip(columns, row))
                    return JsonResponse({'user_profile': profile_data})
                else:
                    return JsonResponse({'message': 'User profile not found'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Only GET requests are allowed'})

@csrf_exempt
def user_authentication(request): #path is: localhost:8000/accounts/user-auth/
    if request.method == 'POST':
        email = request.POST.get('email')  # Assuming email is passed from the form
        password = request.POST.get('password')  # Assuming password is passed from the form
        
        with connection.cursor() as cursor:
            cursor.callproc('SPUserAuthorization', [email, password])
            results = cursor.fetchall()

            if results:
                # If a valid tuple is returned, it means the user is authenticated
                user_data = { #to be altered accordingly to what is sent
                    'user_email': results[0][0],
                    'role_id': results[0][1],
                    'user_type': results[0][2],
                    'user_display_name': results[0][3],
                    'user_phone': results[0][4]
                }
                return JsonResponse({'authenticated': True, 'user_data': user_data})
            else:
                # If no tuple is returned, it means authentication failed
                return JsonResponse({'authenticated': False, 'message': 'Invalid email or password'})
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'})
    

@csrf_exempt  # Disable CSRF protection for simplicity; consider enabling in production
def insert_user_details(request): #path is: localhost:8000/accounts/register-user/
    if request.method == 'POST':
        user_type = request.POST.get('user_type')  # Assuming user_type is passed from the form
        json_data = request.POST.get('json_data')  # Assuming json_data is passed from the form
        
        with connection.cursor() as cursor:
            cursor.callproc('SPInsertUserDetails', [user_type, json_data])
            # Commit the transaction
            connection.commit()

            # Return success response
            return JsonResponse({'message': 'User details inserted successfully'})
    else:
        # Return error response for non-POST requests
        return JsonResponse({'message': 'Only POST requests are allowed'})