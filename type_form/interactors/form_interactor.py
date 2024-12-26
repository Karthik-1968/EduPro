from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,MissingName,FormAlreadyExists,InvalidWorkspace,InvalidUser
from type_form.interactors.storage_interfaces.storage_interface import Formdto


class FormInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter 

    def create_form(self,user_id:uuid,workspace_id:int,name:str):
        """
            ELP:
                check if input data exists
                check if form exists
                create form
        """

        self.validate_input_fields_for_create_form(user_id = user_id,workspace_id = workspace_id,name = name)

        try:
            self.storage.check_if_form_already_exists(name = name)
        except FormAlreadyExists:
            self.presenter.raise_exception_for_form_already_exists()

        userdto=self.storage.get_user(id = user_id)
        workspacedto=self.storage.get_workspace(id = workspace_id)

        formdto = Formdto(user = userdto, workspace = workspacedto, name =name)
        form_id = self.storage.create_form(formdto = formdto)

        return self.presenter.get_response_for_create_form(id = form_id)

    def validate_input_fields_for_create_form(self,user_id:uuid,workspace_id:int,name:str):

        try:
            self.storage.valid_userid_field(id = user_id)
        except MissingId:
            self.raise_exception_for_missing_userid()

        try:
            self.storage.valid_id_field(id = workspace_id)
        except MissingId:
            self.raise_exception_for_missing_workspaceid()

        try:
            self.storage.valid_name_field(name = name)
        except MissingName:
            self.raise_exception_for_missing_form_name()

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

    def get_forms_of_user(self,user_id:uuid):

        """
            ELP:
                check if input data exists
                check if user exists
                get list of forms of user
        """

        try:
            self.storage.valid_userid_field(id = user_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_userid()

        try:
            self.storage.check_user(id = user_id)
        except InvalidUser:
            self.presenter.raise_exception_for_invalid_user()

        formdtos=self.storage.get_forms_of_user(id = user_id)

        return self.presenter.get_response_for_forms_of_user(formdtos = formdtos)