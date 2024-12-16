from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingEmail,InvalidUser

class Create_login_interactor:
    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def login(self,user_email:str,presenter:PresenterInterface):
        try:
            self.storage.valid_email_field(email=user_email)
        except MissingEmail:
            return presenter.raise_exception_for_missing_email()
        
        auth_tokens=self.storage.login(user_email=user_email)
        return presenter.get_login_response(auth_tokens)