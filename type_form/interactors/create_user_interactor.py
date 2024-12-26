from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingEmail,UserAlreadyPresent,MissingId
import uuid
from type_form.interactors.storage_interfaces.storage_interface import Userdto

class CreateUserInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage = storage

    def create_user(self,id:uuid,email:str,presenter:PresenterInterface):
        """
        ELP:
            -validate input fields
                -validate email
            -check if user is already present
            -create user
        """
        try:
            self.storage.valid_userid_field(id = id)
        except MissingId:
            presenter.raise_exception_for_missing_userid()

        try:
            self.storage.valid_email_field(email = email)
        except MissingEmail:
            presenter.raise_exception_for_missing_email()
        
        try:
            self.storage.check_if_user_already_present(email = email)
        except UserAlreadyPresent:
            presenter.raise_exception_for_user_already_present()
        
        userdto=Userdto(id = id,email = email)
        self.storage.create_user(userto = userdto)

        return presenter.get_response_for_create_user()