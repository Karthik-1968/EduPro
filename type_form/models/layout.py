from django.db import models
from .user import User
from .form import Form

class Layout(models.Model):

    form = models.OneToOneField(Form,on_delete=models.CASCADE,related_name="layout")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="layouts")
    layout_name = models.CharField(max_length=100)