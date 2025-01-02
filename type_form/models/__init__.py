from .user import User
from .form import Form
from .field import Field
from .formresponse import FormResponse
from .formfield import FormField
from .formfieldresponse import FormFieldResponse
from .formfieldsettings import FormFieldSettings
from .workspace import Workspace
from .workspaceinvite import WorkspaceInvite

__all__ = [User, Form, Field, FormResponse, FormField, FormFieldResponse, FormFieldSettings, Workspace, WorkspaceInvite]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
