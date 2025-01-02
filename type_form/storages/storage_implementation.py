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
from datetime import datetime

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
    
    def check_workspace(self, id: int):
        workspace_exists = Workspace.objects.filter(id = id).exists()
        workspace_not_exists = not workspace_exists
        if workspace_not_exists:
            raise InvalidWorkspaceException
        
    def check_if_user_already_invited(self, user_id: str, workspace_id: int):
        if WorkspaceInvite.objects.filter(user_id = user_id, workspace_id = workspace_id).exists():
            raise AlreadyInvitedException
        
    def check_if_invites_limit_reached(self, id:int):
        workspace = Workspace.objects.get(id = id)
        if workspace.max_invities == workspace.invites_sent:
            raise MaximumInvitesLimitReachedException
        
    def create_workspace_invite(self, name:str, user_id:str, workspace_id:int, role:int, is_accepted:bool, expiry_time:str):
        
        workspace_invite = WorkspaceInvite.objects.create(name = name, user_id = user_id, workspace_id = workspace_id, role = role,\
            is_accepted = is_accepted, expiry_time = expiry_time)
        
        workspace = Workspace.objects.get(id = workspace_id)
        workspace.invites_sent += 1
        
        return workspace_invite.id
    
    def check_workspace_invite(self, id:int):
        
        workspace_invite_exists = WorkspaceInvite.objects.filter(id = id).exists()
        workspace_invite_not_exists = not workspace_invite_exists
        if workspace_invite_not_exists:
            raise InvalidInvitationException
        
    def check_if_invitation_already_accepted(self, id:int):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        if workspace_invite.is_accepted:
            raise AlreadyAcceptedException
        
    def check_if_invitation_expired(self, id):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        if workspace_invite.expiry_time < datetime.now():
            raise InvitationExpiredException
        
    def accept_invitation(self, id:int):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        workspace_invite.is_accepted = True
        workspace_invite.save()
        
    def reject_invitation(self, id:int):
        
        workspace_invite = WorkspaceInvite.objects.get(id = id)
        workspace_invite.delete()
        
    def get_invities_of_workspace(self, id:int)->list[WorkspaceInviteDTO]:
        
        workspace_invites = WorkspaceInvite.objects.filter(workspace_id = id)
        workspaceinvitedtos = []
        for workspace_invite in workspace_invites:
            workspaceinvitedto = self.convert_workspace_invite_object_to_dto(workspace_invite)
            workspaceinvitedtos.append(workspaceinvitedto)
        
        return workspaceinvitedtos
    
    def convert_workspace_invite_object_to_dto(self, workspace_invite):
        
        return WorkspaceInviteDTO(
            name = workspace_invite.name,
            user_id = workspace_invite.user_id,
            workspace_id = workspace_invite.workspace_id,
            role = workspace_invite.role,
            is_accepted = workspace_invite.is_accepted,
            expiry_time = workspace_invite.expiry_time
        )