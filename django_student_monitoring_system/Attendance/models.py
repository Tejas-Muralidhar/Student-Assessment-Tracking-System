from django.db import models
from Subjects.models import SubjectMaster
from Faculty.models import FacultyMaster
from Students.models import StudentMaster

class AttendanceMaster(models.Model):
    attendenceID = models.AutoField(primary_key=True)
    subjectCode = models.ForeignKey(SubjectMaster, on_delete=models.CASCADE)
    facultyID = models.ForeignKey(FacultyMaster, on_delete=models.CASCADE)
    maxClasses = models.IntegerField()

    def __str__(self):
        return f"{self.subjectCode} - {self.facultyID} - Max Classes: {self.maxClasses}"

class AttendanceRecords(models.Model):
    attendanceID = models.ForeignKey(AttendanceMaster, on_delete=models.CASCADE)
    usn = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    isPresent = models.BooleanField() #boolean or int for classes attended? CHECK
    lastUpdated = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('attendanceID', 'usn')  # Ensures a unique combination of attendanceID and usn

    def __str__(self):
        return f"{self.attendanceID} - {self.usn} - Present: {self.isPresent}"