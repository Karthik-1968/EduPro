from django.db import models
from .form import Form
from .user import User


class FormResponse(models.Model):

    form  = models.ForeignKey(Form,on_delete=models.CASCADE,related_name="formresponses")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="formresponses")
    status = models.CharField(max_length=50,choices=[('submitted','Submitted'),('in progress','In Progress')])
    device = models.CharField(max_length=50,choices=[('desktop','Desktop'),('mobile','Mobile')])
    submitted_at = models.DateTimeField(auto_now_add=True)