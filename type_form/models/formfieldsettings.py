from django.db import models

class FormFieldSettings(models.Model):
    
    multiple_selection = models.BooleanField(null=True,blank=True)
    multiple_selection_scope = models.CharField(max_length=50,choices=[('unlimited','Unlimited'), ('exact number','Exact Number'),\
                                        ('range','Range')],null=True,blank=True)
    choices = models.JSONField(null=True,blank=True)
    exact_number_of_selections = models.IntegerField(null=True,blank=True)
    max_number = models.IntegerField(null=True,blank=True)
    min_number = models.IntegerField(null=True,blank=True)
    max_length = models.IntegerField(null=True,blank=True)
    min_length = models.IntegerField(null=True,blank=True)
    other_option = models.BooleanField(null=True,blank=True)
    vertical_alignment = models.BooleanField(null=True,blank=True)
    alphabetical_order = models.BooleanField(null=True,blank=True)