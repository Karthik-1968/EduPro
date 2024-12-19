from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingEmail,InvalidUser


class CreateUserInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def create_user(self,email:str,presenter:PresenterInterface):
        """
        ELP:
            -validate input fields
                -validate email
            -check if user is already present
            -create user
        """

        try:
            self.storage.valid_email_field(email=email)
        except MissingEmail:
            presenter.raise_exception_for_missing_email()
        
        try:
            self.storage.check_user(email=email)
        except InvalidUser:
            presenter.raise_exception_for_invalid_user()
        
        self.storage.create_user(email=email)
        return presenter.get_user_email_response()