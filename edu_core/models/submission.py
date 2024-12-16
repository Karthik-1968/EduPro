from django.db import models
from .student import Student
from .assignment import Assignment


CHOICE=[('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')]

class Submission(models.Model):
    
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    submitted_at=models.DateTimeField()
    Grade=models.CharField(max_length=10,choices=CHOICE,null=True,blank=True)
    remarks=models.CharField(max_length=100,null=True,blank=True)
