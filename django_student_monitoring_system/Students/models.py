from django.db import models
from Subjects.models import SubjectMaster

class StudentMaster(models.Model):
    usn = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1) # 'M' or 'F'
    dateOfBirth = models.DateField()
    phone = models.CharField(max_length=10, unique=True)
    currentSem = models.IntegerField() #which sem the student is in
    parentNumber = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class StudentSubject(models.Model):
    studentsubjectID = models.AutoField(primary_key=True)
    usn = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    subjectCode = models.ForeignKey(SubjectMaster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usn} - {self.subjectCode}"