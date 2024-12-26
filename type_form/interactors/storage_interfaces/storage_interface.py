from abc import abstractmethod
import uuid
from dataclasses import dataclass
from type_form.interactors.storage_interfaces.storage_interface import Workspacedto,WorkspaceInvitedto,Formdto
from typing import Optional

@dataclass
class Userdto:
    id:uuid
    email:str

@dataclass
class Workspacedto:
    user:Userdto
    id:Optional[int]
    name:str
    is_private:Optional[bool]
    max_invites:int

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
    label:str
    field_type:str
    is_required:Optional[bool]

@dataclass
class FormResponsedto:
    user:Userdto
    form:Formdto
    id:Optional[int]
    data:str
    device:str

@dataclass
class FormFielddto:
    form:Formdto
    field:Fielddto

class StorageInterface:

    @abstractmethod
    def valid_userid_field(self,id:uuid):
        pass
    
    @abstractmethod
    def valid_email_field(self,email:str):
        pass

    @abstractmethod
    def check_if_user_already_present(self,email:str):
        pass
    
    @abstractmethod
    def check_user(self,id:uuid):
        pass

    @abstractmethod
    def create_user(self,userdto:Userdto):
        pass

    @abstractmethod
    def valid_name_field(self,name:str):
        pass

    @abstractmethod
    def check_if_workspace_already_exists(self,name:str):
        pass

    @abstractmethod
    def get_user(self,id:uuid)->Userdto:
        pass

    @abstractmethod
    def create_workspace(self,workspacedto:Workspacedto)->int:
        pass

    @abstractmethod
    def valid_id_field(self,id:int):
        pass

    @abstractmethod
    def check_workspace(self,id:int):
        pass

    @abstractmethod
    def check_if_user_already_invited(self,user_id:uuid,workspace_id::int):
        pass

    @abstractmethod
    def get_workspace(self,id:int)->Workspacedto:
        pass

    @abstractmethod
    def create_workspace_invite(self,workspaceinvitedto:WorkspaceInvitedto)->int:
        pass
    
    @abstractmethod
    def check_invitation(self,id:int):
        pass

    @abstractmethod
    def check_if_invitation_already_accepted(self,id:int):
        pass

    @abstractmethod
    def accept_invitation(self,id:int):
        pass

    @abstractmethod
    def get_workspaces_of_user(self,id:uuid)->list[Workspacedto]:
        pass

    @abstractmethod
    def get_workspaces_of_user(self,id:int)->list[WorkspaceInvitedto]:
        pass

    @abstractmethod
    def check_if_form_already_exists(self,name:str):
        pass

    @abstractmethod
    def create_form(self,formdto:Formdto)->int:
        pass

    @abstractmethod
    def get_forms_of_workspace(self,id:int)->list[Formdto]:
        pass

    @abstractmethod
    def get_forms_of_user(self,id:uuid)->list[Formdto]:
        pass

    @abstractmethod
    def valid_label_field(self,label:str):
        pass

    @abstractmethod
    def valid_field_type_field(self,field_type:str):
        pass

    @abstractmethod
    def check_form(self,id:int):
        pass

    @abstractmethod
    def get_form(self,id:int)->Formdto:
        pass

    @abstractmethod
    def create_field(self,field_dto:Fielddto)->int:
        pass

    @abstractmethod
    def get_fields_of_form(self,id:int)->list[Fielddto]:
        pass

    @abstractmethod
    def check_if_field_already_exists(self,label:str,field_type:str):
        pass

    @abstractmethod
    def valid_device_field(self,device:str):
        pass

    @abstractmethod
    def valid_data_field(self,data:str):
        pass

    @abstractmethod
    def create_form_response(self,formresponsedto:FormResponsedto):
        pass

    @abstractmethod
    def get_responses_of_form(self,id:int)->list[FormResponsedto]:
        pass

    @abstractmethod
    def raise_exception_for_missing_fieldid(self):
        pass

    @abstractmethod
    def check_field(self,id:int):
        pass

    @abstractmethod
    def get_field(self,id:int)->Fielddto:
        pass

    @abstractmethod
    def add_field_to_form(self,formfielddto:FormFielddto):
        pass