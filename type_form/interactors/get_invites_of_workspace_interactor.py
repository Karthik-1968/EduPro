from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import WorkspaceInvitedto
from type_form.exceptions.custom_exceptions import InvalidWorkspace,MissingId

class GetInvitesOfWorkspaceInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage = storage
        self.presenter = presenter

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
        return self.presenter.get_response_for_workspace_invites(workspaceinvitedtos=workspaceinvitedtos)
