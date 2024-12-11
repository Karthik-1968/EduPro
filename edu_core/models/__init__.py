from .student import Student
from .user import User
from .teacher import Teacher
from .course import Course
from .assignment import Assignment
from .submission import Submission
__all__ = [User,Student,Teacher,Course,Assignment,Submission]

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
