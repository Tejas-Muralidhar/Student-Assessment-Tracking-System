from django.db import models
from Subjects.models import SubjectMaster

class FacultyMaster(models.Model):
    facultyID = models.CharField(max_length=10, primary_key=True)
    facultyName = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    facultyPhone = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.facultyName
    

class FacultySubject(models.Model):
    facultySubjectID = models.AutoField(primary_key=True)
    subjectCode = models.ForeignKey(SubjectMaster, on_delete=models.CASCADE)
    facultyID = models.ForeignKey(FacultyMaster, on_delete=models.CASCADE)
    section = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.facultyID} - {self.subjectCode} - {self.section}"
