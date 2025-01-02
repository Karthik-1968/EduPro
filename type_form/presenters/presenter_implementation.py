from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from type_form.constants.exception_messages import MISSING_EMAIL, MISSING_USERID, USER_ALREADY_PRESENT, MISSING_WORKSPACE_NAME,\
    INVALID_USER_ID, INVALID_WORKSPACE_ID, WORKSPACE_ALREADY_EXISTS, USER_ALREADY_INVITED, MAXIMUM_INVITES_REACHED, INVALID_INVITE_ID,\
        INVITATION_EXPIRED
from type_form.interactors.storage_interfaces.storage_interface import WorkspaceDTO, WorkspaceInviteDTO, FormDTO, FieldDTO, \
    FormResponseDTO, FormFieldDTO, FormFieldResponseDTO, PhoneNumberFieldSettingsDTO

class PresenterImplementation(PresenterInterface):
    
    def raise_exception_for_missing_email(self):
        raise NotFound(*MISSING_EMAIL)
    
    def raise_exception_for_missing_userid(self):
        raise NotFound(*MISSING_USERID)
    
    def raise_exception_for_user_already_present(self):
        raise BadRequest(*USER_ALREADY_PRESENT)

    def get_response_for_create_user(self, user_email:str):
        return {
            "user_email": user_email
        }
        
    def raise_excpetion_from_missing_workspace_name(self):
        raise NotFound(*MISSING_WORKSPACE_NAME)
    
    def raise_exception_for_invalid_user_id(self):
        raise BadRequest(*INVALID_USER_ID)
    
    def raise_exception_for_workspace_already_exists(self):
        raise BadRequest(*WORKSPACE_ALREADY_EXISTS)
    
    def raise_exception_for_invalid_workspace_id(self):
        raise NotFound(*INVALID_WORKSPACE_ID)
    
    def get_response_for_create_workspace(self, workspace_id:int):
        return {
            "workspace_id": workspace_id
        }
        
    def get_response_for_workspaces_of_user(self, workspacedtos:list[WorkspaceDTO])->list[dict]:
        
        workspaces = []
        for workspace in workspacedtos:
            workspace_dict = {
                "name": workspace.name,
                "is_private": workspace.is_private,
                "max_invites": workspace.max_invites
            }
            workspaces.append(workspace_dict)
        
        return workspaces
    
    def raise_exception_for_invalid_workspace(self):
        raise NotFound(*INVALID_WORKSPACE_ID)
    
    def raise_exception_for_user_already_invited(self):
        raise BadRequest(*USER_ALREADY_INVITED)
    
    def raise_exception_for_maximum_invites_reached(self):
        raise BadRequest(*MAXIMUM_INVITES_REACHED)
    
    def get_response_for_create_workspace_invite(self, id:int):
        return {
            "workspace_invite_id": id
        }
    
    def raise_exception_for_invalid_invite(self):
        raise NotFound(*INVALID_INVITE_ID)
    
    def raise_exception_for_user_already_invited(self):
        raise BadRequest(*USER_ALREADY_INVITED)
    
    def raise_exception_for_invitation_expired(self):
        raise Forbidden(*INVITATION_EXPIRED)
    
    def get_response_for_accept_invitation(self):
        return {"success":"invite accepted successfully"}
    
    def get_response_for_reject_invitation(self):
        return {"success":"invite rejected successfully"}
    
    def get_response_for_workspace_invites(self, workspaceinvitedtos:list[WorkspaceInviteDTO])->list[dict]:
        workspace_invites = []
        for workspace_invite in workspaceinvitedtos:
            workspace_invite_dict = {
                "name": workspace_invite.name,
                "role": workspace_invite.role,
                "is_accepted": workspace_invite.is_accepted,
                "expiry_time": workspace_invite.expiry_time
            }
            workspace_invites.append(workspace_invite_dict)
        
        return workspace_invites
        