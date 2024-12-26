from django.db import models
from .dynamicform import DynamicForm


class SubmittedFormData(models.Model):

    form = models.ForeignKey(DynamicForm,on_delete=models.CASCADE,related_name="submitteddata")
    data = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)