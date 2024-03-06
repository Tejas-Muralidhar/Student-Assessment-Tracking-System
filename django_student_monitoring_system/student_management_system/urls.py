"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('MASTER/', admin.site.urls),
    path('admin/',include("Admin.urls")),
    path('',include("Accounts.urls")),
    path('accounts/',include('Accounts.urls')),
    path('attendance/',include('Attendance.urls')),
    path('faculty/',include('Faculty.urls')),
    path('marks/',include('Marks.urls')),
    path('student/',include('Students.urls')),
    path('subject/',include('Subjects.urls')),
]
#redirect to 'student_management_system.urls' if you want to travel from one app to another