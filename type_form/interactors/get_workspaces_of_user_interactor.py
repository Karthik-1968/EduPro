from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import Workspacedto
import uuid
from type_form.exceptions.custom_exceptions import InvalidUser,MissingId

class GetWorkspacesOfUserInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_workspaces_of_user(self,id:int):

        """
            ELP:
                check if input data exists
                check if user exists
                get list of workspaces of user
        """
        try:
            self.storage.valid_userid_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_userid()

        try:
            self.storage.check_user(id = id)
        except InvalidUser:
            self.presenter.raise_exception_for_invalid_user()

        workspacedtos=self.storage.get_workspaces_of_user(id=id)
        return self.presenter.get_response_for_workspaces_of_user(workspacedtos=workspacedtos)

        