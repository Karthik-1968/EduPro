from type_form.models import User

def user():
    users=User.objects.all()
    if not users:
        print("No")
    for user in users:
        if user:
            print(user.email)