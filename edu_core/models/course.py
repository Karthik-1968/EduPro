from django.db import models
from .student import Student
from .teacher import Teacher


class Course(models.Model):

    student=models.ManyToManyField(Student,null=True,blank=True)
    teacher=models.ManyToManyField(Teacher,null=True,blank=True)
    name=models.CharField(max_length=100)
    fee=models.IntegerField()
    duration=models.CharField(max_length=100)