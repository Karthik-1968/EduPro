from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import Workspacedto
import uuid
from type_form.exceptions.custom_exceptions import MissingName,InvalidUser,MissingId,WorkspaceAlreadyExists,InvalidWorkspace

class WorkspaceInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_workspace(self,user_id:int,name:str,is_private:bool,max_invities:int):

        """
            ELP:
                check if input data exists
                check if user exists
                check if workspace exists
                create workspace
        """
        self.validate_input_data_for_create_workspace(id = user_id,name = name)

        try:
            self.storage.check_user(id = user_id)
        except InvalidUser:
            self.presenter.raise_exception_for_invalid_user()

        try:
            self.storage.check_if_workspace_already_exists(name = name)
        except WorkspaceAlreadyExists:
            self.presenter.raise_exception_for_workspace_already_exists()

        userdto = self.storage.get_user(id = user_id)
        workspacedto = Workspacedto(user = userdto,name = name,is_private = is_private,max_invities = max_invities)

        workspace_id = self.storage.create_workspace(workspacedto = workspacedto)
        
        return self.presenter.get_response_for_create_workspace(id = workspace_id)

    def validate_input_data_for_create_workspace(self,id:uuid,name:name):

        try:
            self.storage.valid_userid_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_userid()
        
        try:
            self.storage.valid_name_field(name = name)
        except MissingName:
            self.presenter.raise_exception_for_missing_workspacename()
    
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

        workspacedtos=self.storage.get_workspaces_of_user(id = id)

        return self.presenter.get_response_for_workspaces_of_user(workspacedtos = workspacedtos)

    def get_invities_of_workspace_interactor(self,id:int):

        """
            ELP:
               check if input data exists
               check if workspace exists
               get list of invites of workspace
        """

        try:
            self.storage.valid_id_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_workspaceid()

        try:
            self.storage.check_workspace(id = id)
        except InvalidWorkspace:
            self.presenter.raise_exception_for_invalid_workspace()

        workspaceinvitedtos = self.storage.get_workspace_invites(id = id)

        return self.presenter.get_response_for_workspace_invites(workspaceinvitedtos = workspaceinvitedtos)


    