from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import FormAlreadyExistsException,InvalidWorkspaceException, InvalidUserException
import uuid

class FormInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter 

    def create_form(self, user_id:str, workspace_id:int, name:str):
        """
            ELP:
                -validate input data
                    -validate user_id
                    -validate workspace_id
                    -validate name
                -check if form exists
                -create form
        """

        self.validate_input_fields_for_create_form(user_id = user_id, workspace_id = workspace_id, name = name)
        
        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()
            
        try:
            self.storage.check_workspace(id = workspace_id)
        except InvalidWorkspaceException:
            self.presenter.raise_exception_for_invalid_workspace()

        try:
            self.storage.check_if_form_already_exists(name = name)
        except FormAlreadyExistsException:
            self.presenter.raise_exception_for_form_already_exists()

        form_id = self.storage.create_form(user_id = user_id, workspace_id = workspace_id, name = name)

        return self.presenter.get_response_for_create_form(id = form_id)

    def validate_input_fields_for_create_form(self, user_id:str, workspace_id:int, name:str):

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_userid()

        workspace_id_not_present = not workspace_id
        if workspace_id_not_present:
            self.presenter.raise_exception_for_missing_workspaceid()

        name_not_present = not name
        if name_not_present:
            self.presenter.raise_exception_for_missing_form_name()

    def get_forms_of_workspace(self, workspace_id:int):

        """
            ELP:
                -validate input data
                    -validate workspace_id
                -check if workspace exists
                -get forms of workspace
        """

        workspace_id_not_present = not workspace_id
        if workspace_id_not_present:
            self.presenter.raise_exception_for_missing_workspaceid()

        try:
            self.storage.check_workspace(id = workspace_id)
        except InvalidWorkspaceException:
            self.presenter.raise_exception_for_invalid_workspace()

       
        formdtos=self.storage.get_forms_of_workspace(id = workspace_id)

        return self.presenter.get_response_for_forms_of_workspace(formdtos = formdtos)

    def get_forms_of_user(self, user_id:str):

        """
            ELP:
                -validate input data
                    -validate user_id
                -check if user exists
                -get list of forms of user
        """

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_userid()

        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()

        formdtos=self.storage.get_forms_of_user(id = user_id)

        return self.presenter.get_response_for_forms_of_user(formdtos = formdtos)