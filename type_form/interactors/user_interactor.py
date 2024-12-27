from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import UserAlreadyPresentException
import uuid
from type_form.interactors.storage_interfaces.storage_interface import Userdto

class UserInteractor:

    def __init__(self, storage:StorageInterface):
        self.storage = storage

    def create_user(self, id:uuid, email:str, presenter:PresenterInterface):
        """
        ELP:
            -validate input field
                -validate id
                -validate email
            -check if user is already present
            -create user
        """
        id_not_present = not id
        if id_not_present:
            presenter.raise_exception_for_missing_userid()

        email_not_present = not email
        if email_not_present:
            presenter.raise_exception_for_missing_email()
        
        try:
            self.storage.check_if_user_already_present(email = email)
        except UserAlreadyPresentException:
            presenter.raise_exception_for_user_already_present()
        
        userdto=Userdto(id = id,email = email)
        self.storage.create_user(userto = userdto)

        return presenter.get_response_for_create_user()