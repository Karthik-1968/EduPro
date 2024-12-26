from type_form.exceptions.custom_exceptions import MissingEmail,InvalidUser
from type_form.models import User

class StorageImplementation(StorageInterface):

    def valid_email_field(self,email:str):
        email_not_present = not email
        if email_not_present:
            raise MissingEmail

    def check_user(self,email:str):
        if User.objects.filter(email = email).exists():
            raise InvalidUser

    def create_user(self,email:str):
        User.objects.create(id="2a5e545d-fab1-467b-b184-c3d232f0a4f8",email = email)