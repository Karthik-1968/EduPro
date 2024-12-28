from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import Workspacedto
import uuid
from type_form.exceptions.custom_exceptions import InvalidUserException, WorkspaceAlreadyExistsException

class WorkspaceInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_workspace(self, user_id:int, name:str, is_private:bool = False, max_invites:int = 5):

        """
            ELP:
                -validate input data
                    - validate id
                    - validate name
                -check if user exists
                -check if workspace exists
                -create workspace
        """
        self.validate_input_data_for_create_workspace(id = user_id, name = name)

        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()

        try:
            self.storage.check_if_workspace_already_exists(name = name)
        except WorkspaceAlreadyExistsException:
            self.presenter.raise_exception_for_workspace_already_exists()

        userdto = self.storage.get_user(id = user_id)
        workspacedto = Workspacedto(user = userdto,name = name,is_private = is_private, max_invites = max_invites)

        workspace_id = self.storage.create_workspace(workspacedto = workspacedto)
        
        return self.presenter.get_response_for_create_workspace(workspace_id = workspace_id)

    def validate_input_data_for_create_workspace(self, id:uuid, name:str):
        
        id_not_present = not id
        if id_not_present:
            self.presenter.raise_exception_for_missing_userid()
        
        name_not_present = not name
        if name_not_present:
            self.presenter.raise_exception_for_missing_workspacename()
    
    def get_workspaces_of_user(self, user_id:int):

        """
            ELP:
                -validate input data
                    -validate user_id
                -check if user exists
                -get list of workspaces of user
        """
        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_userid()

        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()

        workspacedtos=self.storage.get_workspaces_of_user(id = user_id)

        return self.presenter.get_response_for_workspaces_of_user(workspacedtos = workspacedtos)


    