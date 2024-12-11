from edu_core.models import Student,Teacher
def usr():
   students=Student.objects.all()
   for s in students:
      print(s.email)
   teachers=Teacher.objects.all()
   for t in teachers:
      print(t.email)