from django.db import models
from .user import User
from .layout import Layout

class Tab(models.Model):

    layout = models.ForeignKey(Layout,on_delete=models.CASCADE,related_name="tabs")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tabs")
    tab_name = models.CharField(max_length=100)
    tab_type = models.CharField(max_length=100)
    config = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    """
    config = {
        "sections_config": [
           {

                type: "CUSTOM",
                "field_ids": List[str]
            },
            {
                type: "DEFAULT",
                "gof_id": str
            }
        ]
    }

    """
