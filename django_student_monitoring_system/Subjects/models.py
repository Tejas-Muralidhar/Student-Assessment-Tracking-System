from django.db import models

class SubjectMaster(models.Model):
    subjectCode = models.CharField(max_length=10, primary_key=True)
    subjectName = models.CharField(max_length=30)
    credits = models.IntegerField()
    sem = models.IntegerField() #in which sem the subject is generally taught
    subjectType = models.BooleanField() #0 for theory and 1 for lab
    isElective = models.BooleanField()
    maxIAMarks = models.IntegerField()
    maxEAMarks = models.IntegerField()
    IA1 = models.IntegerField()
    IA2 = models.IntegerField()
    IA3 = models.IntegerField()
    assignment1 = models.IntegerField()
    assignment2 = models.IntegerField()
    quiz1 = models.IntegerField()
    quiz2 = models.IntegerField()
    labRecord = models.IntegerField()
    labObservation = models.IntegerField()
    labViva = models.IntegerField()

    def __str__(self):
        return self.subjectName
    


