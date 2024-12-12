from edu_core.models import User
def usr():
   user=User.objects.get(email="chaitanyapatcherla46@gmail.com")
   user.user_id="7ca96872-023b-4629-ac94-5b3ccc2b4feb"
   user.save()
   print(user.user_id)
