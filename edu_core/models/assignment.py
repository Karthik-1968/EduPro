from django.db import models
from .course import Course
class Assignment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    max_duration=models.IntegerField()
    assign_description=models.CharField(max_length=100)