from django.db import models
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    age=models.IntegerField()