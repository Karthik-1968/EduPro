from django.db import models
from .user import User

class DynamicForm(models.Model):

    id = models.CharField(primary_key=True,max_length=50)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="forms")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
