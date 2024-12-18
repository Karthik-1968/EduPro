from edu_core.models import Assignment,Course
def usr():
   assignments=Assignment.objects.all()
   for assignment in assignments:
      print(assignment.name,assignment.id)
