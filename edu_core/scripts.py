from edu_core.models import Student,Teacher
def usr():
   students=Student.objects.all()
   for student in students:
      print(student.email)
   print("\n")
   teachers=Teacher.objects.all()
   for teacher in teachers:
      print(teacher.email)
