from django.db import models
from Subjects.models import SubjectMaster
from Students.models import StudentMaster 

class MarksRecords(models.Model):
    marksID = models.AutoField(primary_key=True)
    subjectCode = models.ForeignKey(SubjectMaster, on_delete=models.CASCADE)
    usn = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    IA1Score = models.IntegerField()
    IA2Score = models.IntegerField()
    IA3Score = models.IntegerField(null=True)
    AverageIA = models.IntegerField()
    Assignment1Score = models.IntegerField(null=True)
    Assignment2Score = models.IntegerField(null=True)
    Quiz1Score = models.IntegerField(null=True)
    Quiz2Score = models.IntegerField(null=True)
    labRecordMarks = models.IntegerField(null=True)
    labObservationMarks = models.IntegerField(null=True)
    labVivaMarks = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.usn} - {self.subjectCode} - MarksID: {self.marksID}"

