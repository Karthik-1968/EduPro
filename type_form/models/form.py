from django.db import models
from .user import User
from .workspace import Workspace

class Form(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="forms")
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE,related_name="forms")
    form_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submissions_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0.0)