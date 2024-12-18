from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingEmail,InvalidUserEmail


class LoginInteractor:
    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def login(self,user_email:str,presenter:PresenterInterface):
        """
        ELP:
            -validate input fields
                -validate email
            -check is email is in user emails
            -login
        """

        try:
            self.storage.valid_email_field(email=user_email)
        except MissingEmail:
            return presenter.raise_exception_for_missing_email()
        
        try:
            self.storage.check_if_user_email(email=user_email)
        except InvalidUserEmail:
            return presenter.raise_exception_for_invalid_user_email()
        
        auth_tokens=self.storage.login(user_email=user_email)

        return presenter.get_login_response(auth_tokens)