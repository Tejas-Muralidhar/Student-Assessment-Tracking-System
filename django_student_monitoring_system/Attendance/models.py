from django.db import models
from Subjects.models import SubjectMaster
from Faculty.models import FacultyMaster
from Students.models import StudentMaster

class Attendance(models.Model):
    AttendanceID = models.AutoField(primary_key = True)
    USN = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    FID = models.ForeignKey(FacultyMaster, on_delete=models.CASCADE)
    subjectCode = models.ForeignKey(SubjectMaster, on_delete=models.CASCADE)
    Attended = models.IntegerField()
    MaxClasses = models.IntegerField()
