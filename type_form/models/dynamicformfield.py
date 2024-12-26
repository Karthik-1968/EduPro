from django.db import models
from .dynamicform import DynamicForm


Field_types = [("Text", "Text Field"),
              ("Integer", "Interger Field"),
              ("Float", "Float Field"),
              ("Email", "Email Field"),
              ("Decimal", "Decimal Field"),
              ("Boolean", "Boolean Field"),
              ("DateTime", "DataTime Field"),
              ("UUID", "UUID Field"),
              ("Binary", "Binary Field"),
              ("Date", "Date Field"),
              ("Time", "Time Field"),
              ("JSON", "JSON Field"),
              ("PhoneNumber", "Phone Number Field")]


class DynamicFormField(models.Model):

    form = models.ForeignKey(DynamicForm,on_delete=models.CASCADE,related_name="fields")
    label = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50,choices=Field_types)
    is_required = models.BooleanField()
    placeholder = models.CharField(max_length=100,null=True,blank=True)
