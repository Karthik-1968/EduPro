from django.db import models
from .formfield import FormField
from .formresponse import FormResponse


class FormFieldResponse(models.Model):
    
    form_field = models.ForeignKey(FormField,on_delete=models.CASCADE,related_name="fieldresponses")
    form_response = models.ForeignKey(FormResponse,on_delete=models.CASCADE,related_name="fieldresponses")
    value = models.TextField()