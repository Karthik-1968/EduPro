from type_form.exceptions.custom_exceptions import UserAlreadyPresentException, InvalidUserException, WorkspaceAlreadyExistsException,\
    InvalidWorkspaceException, AlreadyInvitedException, InvalidInvitationException, AlreadyAcceptedException,\
        FormAlreadyExistsException, InvalidFormException, FieldAlreadyExistsException, InvalidFieldException,\
            MaximumInvitesLimitReachedException, SettingsAlreadyExistsException, InvalidFormFieldException,\
                InvalidSettingsException, InvitationExpiredException
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.models import User, Workspace, Form, Field, FormResponse, FormField, FormFieldResponse, FormFieldSettings,\
    WorkspaceInvite
from type_form.interactors.storage_interfaces.storage_interface import UserDTO, WorkspaceDTO, FormDTO, FieldDTO, FormFieldDTO, \
    FormResponseDTO, FormFieldResponseDTO, WorkspaceInviteDTO, PhoneNumberFieldSettingsDTO

class StorageImplementation(StorageInterface):
    
    def check_if_user_already_present(self, email: str):
        
        if User.objects.filter(email = email).exists():
            raise UserAlreadyPresentException
        
    def create_user(self, id: str, email: str)->str:
        User.object.create(id = id, email = email)
        
        return email
    
    def check_user(self, id: str):
        
        user_exists = User.objects.filter(id = id).exists()
        user_not_exists = not user_exists
        if user_not_exists:
            raise InvalidUserException
        
    def check_if_workspace_already_exists(self, name: str):
        
        if Workspace.objects.filter(name = name).exists():
            raise WorkspaceAlreadyExistsException
        
    def create_workspace(self, user_id: str, name: str, is_private: bool, max_invites: int)->int:
        
        workspace = Workspace.objects.create(user_id = user_id, name = name, is_private = is_private, max_invites = max_invites)
        
        return workspace.id
    
    def get_workspaces_of_user(self, id:str)->list[WorkspaceDTO]:
        
        workspaces = Workspace.objects.filter(user_id = id)
        workspacedtos = []
        for workspace in workspaces:
            workspacedto = self.convert_workspace_object_to_dto(workspace)
            workspacedtos.append(workspacedto)
        
        return workspacedtos
    
    def convert_workspace_objects_to_dtos(workspace):
        
        return WorkspaceDTO(
            user_id = workspace.user_id,
            name = workspace.name,
            is_private = workspace.is_private,
            max_invites = workspace.max_invites
        )