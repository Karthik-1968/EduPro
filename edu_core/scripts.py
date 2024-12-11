from edu_core.models import Submission
def usr():
   submissions=Submission.objects.all()
   for submission in submissions:
      print(submission.id,submission.student.name,submission.assignment.name)
