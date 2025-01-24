from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from type_form.constants import exception_messages 
from type_form.interactors.storage_interfaces.storage_interface import WorkspaceDTO, WorkspaceInviteDTO, FormDTO, \
    FormResponseDTO, FormFieldDTO, TabDTO, LayoutDetailsDTO

class PresenterImplementation(PresenterInterface):
    
    def raise_exception_for_missing_email(self):
        raise NotFound(*exception_messages.MISSING_EMAIL)
    
    def raise_exception_for_missing_userid(self):
        raise NotFound(*exception_messages.MISSING_USERID)
    
    def raise_exception_for_user_already_present(self):
        raise BadRequest(*exception_messages.USER_ALREADY_PRESENT)

    def get_response_for_create_user(self, user_email:str):
        return {
            "user_email": user_email
        }
        
    def raise_excpetion_from_missing_workspace_name(self):
        raise NotFound(*exception_messages.MISSING_WORKSPACE_NAME)
    
    def raise_exception_for_invalid_user_id(self):
        raise BadRequest(*exception_messages.INVALID_USER_ID)
    
    def raise_exception_for_workspace_already_exists(self):
        raise BadRequest(*exception_messages.WORKSPACE_ALREADY_EXISTS)
    
    def raise_exception_for_invalid_workspace_id(self):
        raise NotFound(*exception_messages.INVALID_WORKSPACE_ID)
    
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
        raise NotFound(*exception_messages.INVALID_WORKSPACE_ID)
    
    def raise_exception_for_user_already_invited(self):
        raise BadRequest(*exception_messages.USER_ALREADY_INVITED)
    
    def raise_exception_for_maximum_invites_reached(self):
        raise BadRequest(*exception_messages.MAXIMUM_INVITES_REACHED)
    
    def get_response_for_create_workspace_invite(self, id:int):
        return {
            "workspace_invite_id": id
        }
    
    def raise_exception_for_invalid_invite(self):
        raise NotFound(*exception_messages.INVALID_INVITE_ID)
    
    def raise_exception_for_user_already_invited(self):
        raise BadRequest(*exception_messages.USER_ALREADY_INVITED)
    
    def raise_exception_for_invitation_expired(self):
        raise Forbidden(*exception_messages.INVITATION_EXPIRED)
    
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
        raise NotFound(*exception_messages.MISSING_FORM_NAME)
    
    def raise_exception_for_form_already_exists(self):
        raise BadRequest(*exception_messages.FORM_ALREADY_EXISTS)
    
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
        raise NotFound(*exception_messages.MISSING_FIELD_NAME)
    
    def raise_exception_for_missing_field_type(self):
        raise NotFound(*exception_messages.MISSING_FIELD_TYPE)
    
    def raise_exception_for_field_already_exists(self):
        raise BadRequest(*exception_messages.FIELD_ALREADY_EXISTS)
    
    def get_response_for_create_field(self, id:int):
        return {
            "field_id": id
        }
        
    def raise_exception_for_invalid_form(self):
        raise NotFound(*exception_messages.INVALID_FORM_ID)
    
    def raise_exception_for_invalid_field(self):
        raise NotFound(*exception_messages.INVALID_FIELD_ID)
    
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
        raise NotFound(*exception_messages.MISSING_STATUS)
    
    def raise_exception_for_missing_device(self):
        raise NotFound(*exception_messages.MISSING_DEVICE)
    
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
        raise BadRequest(*exception_messages.SETTINGS_ALREADY_EXISTS)
    
    def get_response_for_create_settings(self, id:int):
        return {
            "settings_id": id
        }
        
    def get_response_for_add_settings_to_form_field(self):
        return {"success":"settings added to form field successfully"}
    
    def raise_exception_for_missing_workspaceid(self):
        raise NotFound(*exception_messages.SSING_WORKSPACE_ID)
    
    def raise_exception_for_missing_invite_id(self):
        raise NotFound(*exception_messages.MISSING_INVITE_ID)
    
    def raise_exception_for_missing_formid(self):
        raise NotFound(*exception_messages.MISSING_FORM_ID)
    
    def raise_exception_for_missing_fieldid(self):
        raise NotFound(*exception_messages.MISSING_FIELD_ID)
    
    def raise_exception_for_missing_form_field_id(self):
        raise NotFound(*exception_messages.MISSING_FORM_FIELD_ID)
    
    def raise_exception_for_missing_settings_id(self):
        raise NotFound(*exception_messages.MISSING_SETTINGS_ID)
    
    def raise_exception_for_invalid_form_field(self):
        raise NotFound(*exception_messages.INVALID_FORM_FIELD_ID)
    
    def raise_exception_for_invalid_settings(self):
        raise NotFound(*exception_messages.INVALID_SETTINGS_ID)
    
    def get_response_for_submissions_count_of_form(self, count_of_submissions:int):
        return {
            "count_of_submissions": count_of_submissions
        }
        
    def get_response_for_form_completion_rate(self, completion_rate:float):
        return {
            "completion_rate": completion_rate
        }
        
    def get_response_for_views_count_of_form(self, count_of_views:int):
        return {
            "count_of_views": count_of_views
        }

    def raise_exception_for_layout_already_exists(self):
        raise BadRequest(*exception_messages.LAYOUT_ALREADY_EXISTS)

    def raise_exception_for_tab_already_exists(self):
        raise BadRequest(*exception_messages.TAB_ALREADY_EXISTS)

    def raise_exception_for_invalid_layout(self):
        raise NotFound(*exception_messages.INVALID_LAYOUT_ID)

    def raise_exception_for_invalid_tab(self):
        raise NotFound(*exception_messages.INVALID_TAB_ID)

    def get_response_for_create_layout_for_form(self, id:int)->dict:

        return {
            "layout_id": id
        }
    
    def get_response_for_create_tab_for_layout(self, id:int)->dict:

        return {
            "tab_id": id
        }
    
    def get_response_for_create_field_for_tab(self, tabfield_id:int)->dict:

        return {
            "tabfield_id": tabfield_id
        }

    def get_response_for_get_tab_details(self, tab_dto:TabDTO)->dict:

        return {
            "user_id": tab_dto.user_id,
            "layout_id": tab_dto.layout_id,
            "tab_type": tab_dto.tab_type,
            "tab_name": tab_dto.tab_name,
            "gofs": tab_dto.gofs,
            "form_fields": tab_dto.form_fields,
        }

    def raise_exception_for_invalid_layout(self):
        raise NotFound(*exception_messages.INVALID_LAYOUT_ID)

    def get_response_for_get_layout_details(self, layout_details_dto: LayoutDetailsDTO) -> dict:
        layout_details = {
            "layout_name": layout_details_dto.layout_name,
            "sections_config_tab": self._process_sections_config_tab(layout_details_dto.section_config_tab),
            "form_field_ids_config_tab": self._process_form_field_ids_config_tab(layout_details_dto.form_field_ids_config_tab),
        }
        return layout_details

    def _process_sections_config_tab(self, section_config_tab) -> dict:
        if not section_config_tab:
            return {}
        
        tab_dict = self._create_tab_dict(section_config_tab)
        gof_name_count = 1
        formfield_ids_count = 1

        for section_config in section_config_tab.section_configs:
            if section_config.section_type == "group_name":
                tab_dict[f"group_name_{gof_name_count}"] = section_config.gof
                gof_name_count += 1
            elif section_config.section_type == "form_field_ids":
                tab_dict[f"form_field_ids_{formfield_ids_count}"] = section_config.formfields
                formfield_ids_count += 1

        return tab_dict

    def _process_form_field_ids_config_tab(self, form_field_ids_config_tab) -> dict:
        if not form_field_ids_config_tab:
            return {}

        tab_dict = self._create_tab_dict(form_field_ids_config_tab)
        tab_dict.update({
            "name": form_field_ids_config_tab.name,
            "dob": form_field_ids_config_tab.dob,
            "contact_information": form_field_ids_config_tab.contact_information,
            "work_experience": form_field_ids_config_tab.work_experience,
            "signature": form_field_ids_config_tab.signature,
            "date": form_field_ids_config_tab.date,
        })
        return tab_dict

    def _create_tab_dict(self, tab_dto) -> dict:
        return {
            "tab_id": tab_dto.tab_id,
            "user_id": tab_dto.user_id,
            "tab_type": tab_dto.tab_type,
            "tab_name": tab_dto.tab_name,
        }
