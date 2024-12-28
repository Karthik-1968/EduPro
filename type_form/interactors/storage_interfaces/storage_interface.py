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
    id:int = None

@dataclass 
class WorkspaceInvitedto:
    user: Userdto
    workspace: Workspacedto
    id:Optional[int]
    is_accepted:Optional[bool]
    role:str

@dataclass
class Formdto:
    user:Userdto
    workspace:Workspacedto
    id:Optional[int]
    name:str

@dataclass
class Fielddto:
    id:Optional[int]
    field_name:str
    field_type:str
    is_required:Optional[bool]

@dataclass
class FormResponsedto:
    user:Userdto
    form:Formdto
    id:Optional[int]
    data:str
    device:str
    status:str

@dataclass
class FormFielddto:
    form:Formdto
    user:Userdto
    field:Fielddto
    label:str

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
    def create_workspace_invite(self, workspaceinvitedto:WorkspaceInvitedto)->int:
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
    def create_form(self, formdto:Formdto)->int:
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
    def create_field(self, field_dto:Fielddto)->int:
        pass

    @abstractmethod
    def get_fields_of_form(self, id:int)->list[Fielddto]:
        pass

    @abstractmethod
    def check_if_field_already_exists(self, field_type:str):
        pass

    @abstractmethod
    def create_form_response(self, formresponsedto:FormResponsedto):
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
    def add_field_to_form(self, formfielddto:FormFielddto):
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