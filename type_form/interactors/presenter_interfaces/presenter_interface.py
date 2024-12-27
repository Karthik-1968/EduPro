from abc import abstractmethod
from type_form.interactors.storage_interfaces.storage_interface import Workspacedto,WorkspaceInvitedto,Formdto,Fielddto

class PresenterInterface:

    @abstractmethod
    def raise_exception_for_missing_userid(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_email(self):
        pass
    
    @abstractmethod
    def raise_exception_for_user_already_present(self):
        pass
    
    @abstractmethod
    def get_response_for_create_user(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_workspacename(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_workspace_by_name(self):
        pass

    @abstractmethod
    def get_response_for_create_workspace(self,id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_workspaceid(self):
        pass

    @abstractmethod
    def get_response_for_create_workspace(self):
        pass

    @abstractmethod
    def raise_exception_for_user_already_invited(self):
        pass

    @abstractmethod
    def get_response_for_create_workspace_invite(self,id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_invite_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_invite(self):
        pass

    @abstractmethod
    def raise_exception_for_invitation_already_accepted(self):
        pass

    @abstractmethod
    def get_response_for_accept_invitation(self):
        pass

    @abstractmethod
    def get_response_for_workspaces_of_user(workspacedtos:list[Workspacedto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_workspace(self):
        pass

    @abstractmethod
    def get_response_for_workspace_invites(self,workspaceinvitedtos:list[WorkspaceInvitedto]):
        pass

    @abstractmethod
    def raise_exception_for_missing_form_name(self,name:str):
        pass

    @abstractmethod
    def raise_exception_for_form_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_form(self,id:int):
        pass 

    @abstractmethod
    def raise_exception_for_workspace_already_exists(self):
        pass

    @abstractmethod
    def get_forms_of_workspace_response(self,formdtos:list[Formdto]):
        pass

    @abstractmethod
    def get_response_for_forms_of_user(self,formdtos:list[Formdto]):
        pass

    @abstractmethod
    def raise_exception_for_missing_formid(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_label(self,label:str):
        pass

    @abstractmethod
    def raise_exception_for_missing_field_type(self,field_type:str):
        pass

    @abstractmethod
    def raise_exception_for_invalid_form(self):
        pass

    @abstractmethod
    def get_response_for_create_field(self,id:int):
        pass

    @abstractmethod
    def get_response_for_fields_of_form(self,fielddtos:list[Fielddto]):
        pass

    @abstractmethod
    def raise_exception_for_field_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_data(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_device(self):
        pass

    @abstractmethod
    def get_response_for_create_form_response(self,id:int):
        pass

    @abstractmethod
    def get_response_for_responses_of_form(self,formresponsedtos:list[FormResponsedto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_field(self):
        pass

    @abstractmethod
    def get_response_for_add_field_to_form(self):
        pass

    @abstractmethod
    def get_response_for_views_of_form(self,count_of_views:int):
        pass

    @abstractmethod
    def get_response_for_submissions_of_form(self,count_of_submissions:int):
        pass

    @abstractmethod
    def get_response_for_from_completionrate(self,completion_rate:float):
        pass

    @abstractmethod
    def raise_exception_for_missing_status(self):
        pass
    
    @abstractmethod
    def get_response_for_reject_invitation(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_role(self):
        pass
    
    @abstractmethod
    def raise_exception_for_maximum_invites_reached(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_fieldid(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_invite_name(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_field_name(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_formfield_label(self):
        pass