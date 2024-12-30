from abc import abstractmethod
import uuid
from dataclasses import dataclass
from typing import Optional

@dataclass
class UserDTO:
    id: uuid
    email: str

@dataclass
class WorkspaceDTO:
    user_id: uuid
    name: str
    is_private: bool
    max_invites: int

@dataclass 
class WorkspaceInviteDTO:
    user_id: uuid
    workspace_id: int
    name: str
    is_accepted: bool
    role: str

@dataclass
class FormDTO:
    user_id: uuid
    workspace_id: int
    name: str

@dataclass
class FieldDTO:
    field_name: str
    field_type: str

@dataclass
class FormResponseDTO:
    user_id: uuid
    form_id: int
    device: str
    status: str

@dataclass
class FormFieldDTO:
    form_id: int
    user_int: uuid
    field_id: int
    label: str
    is_required: bool
    group_name: Optional[str] = None
    settings_id: Optional[int] = None
    
@dataclass
class FormFieldResponseDTO:
    form_field_id: int
    form_response_id: int
    field_value: str
@dataclass
class PhoneNumberFieldSettingsDTO:
    country: str
    code: str
    
@dataclass
class FormFieldSettingsDTO:
    multiple_selection: bool = None
    multiple_selection_scope: list[str] = None
    choices: list[str] = None
    phone_number_choices: list[PhoneNumberFieldSettingsDTO] = None
    max_number: int = None
    min_number: int = None
    max_length: int = None
    min_length: int = None
    other_option: bool = None
    vetical_alignment: bool = None
    alphabetical_order: bool = None
    placeholder: str = None
    

class StorageInterface:

    @abstractmethod
    def check_if_user_already_present(self, email:str):
        pass
    
    @abstractmethod
    def check_user(self, id:uuid):
        pass

    @abstractmethod
    def create_user(self, id:uuid, email:str)->uuid:
        pass

    @abstractmethod
    def check_if_workspace_already_exists(self, name:str):
        pass

    @abstractmethod
    def get_user(self, id:uuid)->UserDTO:
        pass

    @abstractmethod
    def create_workspace(self, user_id:uuid, name:str, is_private:bool, max_invites:int)->int:
        pass

    @abstractmethod
    def check_workspace(self, id:int):
        pass

    @abstractmethod
    def check_if_user_already_invited(self, user_id:uuid, workspace_id:int):
        pass

    @abstractmethod
    def get_workspace(self, id:int)->WorkspaceDTO:
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
    def get_workspaces_of_user(self, id:uuid)->list[WorkspaceDTO]:
        pass

    @abstractmethod
    def check_if_form_already_exists(self, name:str):
        pass

    @abstractmethod
    def create_form(self, user_id:uuid, workspace_id:int, name:str)->int:
        pass

    @abstractmethod
    def get_forms_of_workspace(self, id:int)->list[FormDTO]:
        pass

    @abstractmethod
    def get_forms_of_user(self, id:uuid)->list[FormDTO]:
        pass

    @abstractmethod
    def check_form(self, id:int):
        pass

    @abstractmethod
    def get_form(self, id:int)->FormDTO:
        pass

    @abstractmethod
    def create_field(self, field_name:str, field_type:str)->int:
        pass

    @abstractmethod
    def get_fields_of_form(self, id:int)->list[FieldDTO]:
        pass

    @abstractmethod
    def check_if_field_already_exists(self, field_type:str):
        pass

    @abstractmethod
    def create_form_response(self, user_id:uuid, form_id:int, data:str, device:str, status:str)->int:
        pass

    @abstractmethod
    def get_responses_of_form(self, id:int)->list[FormResponseDTO]:
        pass

    @abstractmethod
    def check_field(self, id:int):
        pass

    @abstractmethod
    def get_field(self, id:int)->FieldDTO:
        pass

    @abstractmethod
    def add_field_to_form(self, form_id:int, user_id:uuid, field_id:int, label:str, is_required:bool):
        pass

    @abstractmethod
    def get_views_count_of_form(self, id:int)->int:
        pass

    @abstractmethod
    def get_submissions_count_of_form(self, id:int)->int:
        pass 

    @abstractmethod
    def get_form_completion_rate(self, id:int)->float:
        pass

    @abstractmethod
    def reject_invitation(self, id:int):
        pass
    
    @abstractmethod
    def check_if_invites_limit_reached(self, id:int):
        pass
    
    @abstractmethod
    def get_invites_of_workspace(self, id:int)->list[WorkspaceInviteDTO]:
        pass
    
    @abstractmethod
    def get_responses_of_user(self, id:uuid)->list[FormResponseDTO]:
        pass