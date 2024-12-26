from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,InvalidWorkspace
from type_form.interactors.storage_interfaces.storage_interface import Formdto

class GetFormsOfWorkspaceInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def get_forms_of_workspace(self,id:int):

        """
            ELP:
                check if input data exists
                check if workspace exists
                get forms of workspace
        """

        try:
            self.storage.valid_id_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_workspaceid()

        try:
            self.storage.check_workspace(id = id)
        except InvalidWorkspace:
            self.presenter.raise_exception_for_invalid_workspace()

       
        formdtos=self.storage.get_forms_of_workspace(id = id)
        return presenter.get_forms_of_workspace_response(formdtos = formdtos)