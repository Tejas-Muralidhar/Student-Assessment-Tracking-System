from django.db import models

class Roles(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=20)
    '''
    Roles: 
    1: View and Download
    2: Edit their own student and subject marks and attendance
    3: Master Edit 
    '''

    def __str__(self):
        return self.roleName


class Users(models.Model):
    userID = models.AutoField(primary_key=True)  
    userEmail = models.CharField(max_length=50, unique=True)
    userPassword = models.CharField(max_length=20)
    roleId = models.ForeignKey(Roles, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userEmail
