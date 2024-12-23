from django.db import models
from .User import User

class DynamicForm(models.Model):

    id = models.IntegerField(primary_key=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
