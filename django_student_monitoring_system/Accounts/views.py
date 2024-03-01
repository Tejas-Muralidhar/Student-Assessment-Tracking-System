from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.db import connection
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
import json
from django.conf import settings

def UserProfile(user_type_key): 
    try:
        
        with connection.cursor() as cursor:
            cursor.callproc('SPUserProfile', [user_type_key])
            # Fetch all the results
            results = cursor.fetchall()
            # Close the cursor explicitly
            
            if results:
                # Assuming SPUserProfile returns a single row, you can directly access the first row
                row = results[0]
                columns = [col[0] for col in cursor.description]
                # Convert row to dictionary
                profile_data = dict(zip(columns, row))
                return profile_data 
            else:
                return None
    except Exception as e:
        # Log the exception for debugging purposes
        print("Error fetching user profile:", e)
        # Return None or an appropriate error message
        return 500



@csrf_exempt
def UserAuthorization(request): #path is: localhost:8000/accounts/user-auth/
    if request.method == 'POST': 
        email = request.POST.get('email')  # Assuming email is passed from the form
        password = request.POST.get('password')  # Assuming password is passed from the form

        try:
            with connection.cursor() as cursor:
                cursor.callproc('SPUserAuthorization', [email, password]) #PROCUDURE SHOULD SEND BACK USER_TYPE_KEY I.E FACID OR USN
                results = cursor.fetchall()
                cursor.close()
                if results:
                    # If a valid tuple is returned, it means the user is authenticated
                    user_data = { #to be altered accordingly to what is sent
                        'user_email': results[0][0],
                        'user_type': results[0][1],
                        'user_type_key': results[0][2],
                        'user_display_name': results[0][3],  
                        'user_phone': results[0][4],
                    }

                    if user_data['user_type'] == 'Faculty':
                        data = UserProfile(user_data['user_type_key']) #WE SEND FACID TO USER PROFILE TO GET BACK THE DATA OF THE PROFILE OF THE FACULTY
                        if data == None:
                            return JsonResponse({'message': 'No user profile was found with the given credentials'}, status=500)
                        elif data == 500:
                            return JsonResponse({'message': 'Server Error. Try again...'}, status=500)
                        else:
                            return render(request,"FacultyDash.html",data) #ALSO SEND BACK data so that we can use those variables in the HTML PAGE
                    
                    elif user_data['user_type'] == 'Student':
                        data = UserProfile(user_data['user_type_key']) #WE SEND USN TO USER PROFILE TO GET BACK THE DATA OF THE PROFILE OF THE STUDENT
                        if data == None:
                            return JsonResponse({'message': 'No user profile was found with the given credentials'}, status=500)
                        elif data == 500:
                            return JsonResponse({'message': 'Server Error. Try again...'}, status=500)
                        else:
                            return render(request,"StudentDash.html",data) #ALSO SEND BACK data so that we can use those variables in the HTML PAGE
                        
                    elif user_data['user_type'] == 'Admin':
                        data = UserProfile(user_data['user_type_key']) #WE SEND USN TO USER PROFILE TO GET BACK THE DATA OF THE PROFILE OF THE STUDENT
                        if data == None:
                            return JsonResponse({'message': 'No user profile was found with the given credentials'}, status=500)
                        elif data == 500:
                            return JsonResponse({'message': 'Server Error. Try again...'}, status=500)
                        else:
                            return render(request,"Admin.html",data) #ALSO SEND BACK data so that we can use those variables in the HTML PAGE
                    else:
                        return JsonResponse({'authenticated': True, 'user_data': user_data})
                else:
                    # If no tuple is returned, it means authentication failed
                    return JsonResponse({'authenticated': False, 'message': 'Invalid email or password'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'})
    
@csrf_exempt
def InsertUserDetails(request): #path is: localhost:8000/accounts/register-user/
    if request.method == 'POST':
        user_type = request.POST.get('user_type')  # Assuming user_type is passed from the form
        json_data = request.POST.get('json_data')  # Assuming json_data is passed from the form


        # ~~~~~~~~~~~~~~~
        #to check if the post request works:
        # data = {
        #         "facultyID": "FAC011",
        #         "facultyName": "Mrs.Meenakshi",
        #         "gender": "F",
        #         "facultyPhone": "7803210",
        #         "userEmail": "meenaki@gmal.com",
        #         "userPassword": "21356",
        #         "roleId_id": "2"
        #         }
        
        # json_data = json.dumps(data)
        # ~~~~~~~~~~~~~~~
        
        with connection.cursor() as cursor:
            cursor.callproc('SPInsertUserDetails', [user_type, json_data])
            # Commit the transaction
            connection.commit()

            # Return success response
            return JsonResponse({'message': 'User details inserted successfully'})
    else:
        # Return error response for non-POST requests
        return JsonResponse({'message': 'Only POST requests are allowed'})
    
def Login(request):
    return render(request,"Login.html")


@never_cache
def logout_view(request):
    print('HELLO')
    return redirect('Login') 