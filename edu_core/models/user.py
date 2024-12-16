from django.db import models
import uuid


class User(models.Model):

    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email = models.EmailField(null=False, blank=False,unique=True)