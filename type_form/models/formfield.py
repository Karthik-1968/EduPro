from django.db import models
from .form import Form
from .field import Field
from .user import User
from .formfieldsettings import FormFieldSettings

class FormField(models.Model):
    
    form = models.ForeignKey(Form,on_delete=models.CASCADE,related_name="formfields")
    field = models.ForeignKey(Field,on_delete=models.CASCADE,related_name="formfields")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="formfields")
    settings = models.ForeignKey(FormFieldSettings,on_delete=models.CASCADE,related_name="formfields",null=True,blank=True)
    group_name = models.CharField(max_length=100,null=True,blank=True)
    label_text = models.CharField(max_length=100,null=True,blank=True)
    label_vedio = models.CharField(max_length=100,null=True,blank=True)
    is_required = models.BooleanField(default=False)