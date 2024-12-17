from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingEmail,InvalidUser

class create_user_interactor():

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def create_user(self,user_email:str,presenter:PresenterInterface):

        try:
            self.storage.valid_email_field(email=user_email)
        except MissingEmail:
            return presenter.raise_exception_for_missing_email()
        
        try:
            self.storage.check_user(email=user_email)
        except InvalidUser:
            return presenter.raise_exception_for_invalid_user()
        
        self.storage.create_user(email=user_email)
        return presenter.get_user_email_response()