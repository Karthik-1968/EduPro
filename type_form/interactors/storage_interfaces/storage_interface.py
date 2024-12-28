from abc import abstractmethod
import uuid
from dataclasses import dataclass
from typing import Optional

@dataclass
class Userdto:
    id:uuid
    email:str

@dataclass
class Workspacedto:
    user:Userdto
    name:str
    is_private:bool
    max_invites:int

@dataclass 
class WorkspaceInvitedto:
    user_id: uuid
    workspace_id: int
    name: str
    is_accepted: bool
    role: str

@dataclass
class Formdto:
    user_id:uuid
    workspace_id:int
    name:str

@dataclass
class Fielddto:
    field_name:str
    field_type:str

@dataclass
class FormResponsedto:
    user_id:uuid
    form_id:int
    data:str
    device:str
    status:str

@dataclass
class FormFielddto:
    form_id:int
    user_int:uuid
    field_int:int
    label:str
    is_required:bool

class StorageInterface:

    @abstractmethod
    def check_if_user_already_present(self, email:str):
        pass
    
    @abstractmethod
    def check_user(self, id:uuid):
        pass

    @abstractmethod
    def create_user(self, userdto:Userdto)->uuid:
        pass

    @abstractmethod
    def check_if_workspace_already_exists(self, name:str):
        pass

    @abstractmethod
    def get_user(self, id:uuid)->Userdto:
        pass

    @abstractmethod
    def create_workspace(self, workspacedto:Workspacedto)->int:
        pass

    @abstractmethod
    def check_workspace(self, id:int):
        pass

    @abstractmethod
    def check_if_user_already_invited(self, user_id:uuid, workspace_id:int):
        pass

    @abstractmethod
    def get_workspace(self, id:int)->Workspacedto:
        pass

    @abstractmethod
    def create_workspace_invite(self, name:str, user_id:uuid, workspace_id:int, role:str, is_accepted:bool)->int:
        pass
    
    @abstractmethod
    def check_invitation(self, id:int):
        pass

    @abstractmethod
    def check_if_invitation_already_accepted(self, id:int):
        pass

    @abstractmethod
    def accept_invitation(self, id:int):
        pass

    @abstractmethod
    def get_workspaces_of_user(self, id:uuid)->list[Workspacedto]:
        pass

    @abstractmethod
    def check_if_form_already_exists(self, name:str):
        pass

    @abstractmethod
    def create_form(self, user_id:uuid, workspace_id:int, name:str)->int:
        pass

    @abstractmethod
    def get_forms_of_workspace(self, id:int)->list[Formdto]:
        pass

    @abstractmethod
    def get_forms_of_user(self, id:uuid)->list[Formdto]:
        pass

    @abstractmethod
    def check_form(self, id:int):
        pass

    @abstractmethod
    def get_form(self, id:int)->Formdto:
        pass

    @abstractmethod
    def create_field(self, field_name:str, field_type:str)->int:
        pass

    @abstractmethod
    def get_fields_of_form(self, id:int)->list[Fielddto]:
        pass

    @abstractmethod
    def check_if_field_already_exists(self, field_type:str):
        pass

    @abstractmethod
    def create_form_response(self, user_id:uuid, form_id:int, data:str, device:str, status:str)->int:
        pass

    @abstractmethod
    def get_responses_of_form(self, id:int)->list[FormResponsedto]:
        pass

    @abstractmethod
    def check_field(self, id:int):
        pass

    @abstractmethod
    def get_field(self, id:int)->Fielddto:
        pass

    @abstractmethod
    def add_field_to_form(self, form_id:int, user_id:uuid, field_id:int, label:str, is_required:bool):
        pass

    @abstractmethod
    def get_views_of_form(self, id:int)->int:
        pass

    @abstractmethod
    def get_submissions_of_form(self, id:int)->int:
        pass 

    @abstractmethod
    def get_form_completionrate(self, id:int)->float:
        pass

    @abstractmethod
    def reject_invitation(self, id:int):
        pass
    
    @abstractmethod
    def check_if_invites_limit_reached(self, id:int):
        pass
    
    @abstractmethod
    def get_invites_of_workspace(self, id:int)->list[WorkspaceInvitedto]:
        pass
    
    @abstractmethod
    def get_responses_of_user(self, id:uuid)->list[FormResponsedto]:
        pass