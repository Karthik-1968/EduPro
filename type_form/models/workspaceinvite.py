from django.db import models
from .user import User
from .workspace import Workspace


class WorkspaceInvite(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="invites")
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE,related_name="invites")
    role = models.CharField(max_length=50)
    is_accepted = models.BooleanField(default=False)
    expiry_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)