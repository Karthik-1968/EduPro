from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from type_form.constants.exception_messages import MISSING_EMAIL, MISSING_USERID, USER_ALREADY_PRESENT, MISSING_WORKSPACE_NAME,\
    INVALID_USER_ID, INVALID_WORKSPACE_ID, WORKSPACE_ALREADY_EXISTS, USER_ALREADY_INVITED, MAXIMUM_INVITES_REACHED, INVALID_INVITE_ID,\
        INVITATION_EXPIRED, MISSING_FORM_NAME, FORM_ALREADY_EXISTS, MISSING_FIELD_NAME, MISSING_FIELD_TYPE, FIELD_ALREADY_EXISTS,\
            INVALID_FORM_ID, INVALID_FIELD_ID, MISSING_STATUS, MISSING_DEVICE, SETTINGS_ALREADY_EXISTS
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
    
    def raise_exception_for_missing_form_name(self, name:str):
        raise NotFound(*MISSING_FORM_NAME)
    
    def raise_exception_for_form_already_exists(self):
        raise BadRequest(*FORM_ALREADY_EXISTS)
    
    def get_response_for_create_form(self, id:int):
        return {
            "form_id": id
        }
        
    def get_response_for_forms_of_workspace(self, formdtos:list[FormDTO])->list[dict]:
        forms = []
        for form in formdtos:
            form_dict = {
                "name": form.name
            }
            forms.append(form_dict)
        
        return forms
    
    def get_response_for_forms_of_user(self, formdtos:list[FormDTO])->list[dict]:
        forms = []
        for form in formdtos:
            form_dict = {
                "name": form.name
            }
            forms.append(form_dict)
        
        return forms
    
    def raise_exception_for_missing_field_name(self):
        raise NotFound(*MISSING_FIELD_NAME)
    
    def raise_exception_for_missing_field_type(self):
        raise NotFound(*MISSING_FIELD_TYPE)
    
    def raise_exception_for_field_already_exists(self):
        raise BadRequest(*FIELD_ALREADY_EXISTS)
    
    def get_response_for_create_field(self, id:int):
        return {
            "field_id": id
        }
        
    def raise_exception_for_invalid_form(self):
        raise NotFound(*INVALID_FORM_ID)
    
    def raise_exception_for_invalid_field(self):
        raise NotFound(*INVALID_FIELD_ID)
    
    def get_response_for_add_field_to_form(self, id:int):
        return {
            "field_id": id
        }
        
    def get_response_for_fields_of_form(self, formfielddtos:list[FormFieldDTO])->list[dict]:
        formfields = []
        for form_field in formfielddtos:
            form_field_dict = {
                "label_text": form_field.label_text,
                "label_vedio": form_field.label_vedio,
                "group_name": form_field.group_name,
                "is_required": form_field.is_required
            }
            formfields.append(form_field_dict)
        
        return formfields
    
    def raise_exception_for_missing_status(self):
        raise NotFound(*MISSING_STATUS)
    
    def raise_exception_for_missing_device(self):
        raise NotFound(*MISSING_DEVICE)
    
    def get_response_for_responses_of_form(self, formresponse_dtos:list[FormResponseDTO])->list[dict]:
        formresponses = []
        for form_response in formresponse_dtos:
            form_response_dict = {
                "user_id": form_response.user_id,
                "data": form_response.data,
                "device": form_response.device,
                "status": form_response.status
            }
            formresponses.append(form_response_dict)
        
        return formresponses
    
    def get_response_for_responses_of_user(self, formresponse_dtos:list[FormResponseDTO])->list[dict]:
        formresponses = []
        for form_response in formresponse_dtos:
            form_response_dict = {
                "form_id": form_response.form_id,
                "data": form_response.data,
                "device": form_response.device,
                "status": form_response.status
            }
            formresponses.append(form_response_dict)
        
        return formresponses
    
    def raise_exception_for_settings_already_exists(self):
        raise BadRequest(*SETTINGS_ALREADY_EXISTS)
    
    def get_response_for_create_settings(self, id:int):
        return {
            "settings_id": id
        }
        
    def get_response_for_add_settings_to_form_field(self):
        return {"success":"settings added to form field successfully"}