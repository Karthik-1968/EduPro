from abc import abstractmethod
import uuid
from dataclasses import dataclass
from typing import Optional

@dataclass
class UserDTO:
    id: str
    email: str

@dataclass
class WorkspaceDTO:
    user_id: str
    name: str
    is_private: bool
    max_invites: int

@dataclass 
class WorkspaceInviteDTO:
    user_id: str
    workspace_id: int
    name: str
    is_accepted: bool
    role: str

@dataclass
class FormDTO:
    user_id: str
    workspace_id: int
    name: str

@dataclass
class FieldDTO:
    field_name: str
    field_type: str

@dataclass
class FormResponseDTO:
    user_id: str
    form_id: int
    data: str
    device: str
    status: str

@dataclass
class FormFieldDTO:
    form_id: int
    user_id: str
    field_id: int
    label_text: Optional[str]
    label_vedio: Optional[str]
    is_required: bool
    group_name: Optional[str]
    settings_id: Optional[int] 
    
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
class TabDTO:
    tab_id: int
    user_id: str
    layout_id: int
    tab_name: str
    tab_type: str

@dataclass
class SectionConfigDTO:
    section_type: str
    section_name: Optional[str]
    gof: Optional[str]
    formfields: Optional[list[int]]
     
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

@dataclass
class FormFieldIdsConfigDTO:
    name: int
    dob: int 
    contact_information: list[int]
    work_experience: list[int]
    signature: int
    date: int
    

class StorageInterface:

    @abstractmethod
    def check_if_user_already_present(self, email:str):
        pass
    
    @abstractmethod
    def check_user(self, id:str):
        pass

    @abstractmethod
    def create_user(self, id:str, email:str)->str:
        pass

    @abstractmethod
    def check_if_workspace_already_exists(self, name:str):
        pass

    @abstractmethod
    def get_user(self, id:uuid)->UserDTO:
        pass

    @abstractmethod
    def create_workspace(self, user_id:str, name:str, is_private:bool, max_invites:int)->int:
        pass

    @abstractmethod
    def check_workspace(self, id:int):
        pass

    @abstractmethod
    def check_if_user_already_invited(self, user_id:str, workspace_id:int):
        pass

    @abstractmethod
    def get_workspace(self, id:int)->WorkspaceDTO:
        pass

    @abstractmethod
    def create_workspace_invite(self, name:str, user_id:str, workspace_id:int, role:str, is_accepted:bool, expiry_time:str)->int:
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
    def get_workspaces_of_user(self, id:str)->list[WorkspaceDTO]:
        pass

    @abstractmethod
    def check_if_form_already_exists(self, name:str):
        pass

    @abstractmethod
    def create_form(self, user_id:str, workspace_id:int, name:str)->int:
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
    def get_fields_of_form(self, id:int)->list[FormFieldDTO]:
        pass

    @abstractmethod
    def check_if_field_already_exists(self, field_type:str):
        pass

    @abstractmethod
    def create_form_response(self, user_id:str, data:str, form_id:int, device:str, status:str)->int:
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
    def add_field_to_form(self, form_id:int, user_id:str, field_id:int, label_text:str, label_vedio:str, group_name:str,\
        setting_id:int, is_required:bool)->int:
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
    
    @abstractmethod
    def check_if_settings_exists(self, multiple_selection:bool=None, multiple_selection_scope:list[str]=None, choices:list[str]=None,\
        phone_number_choices:list[PhoneNumberFieldSettingsDTO]=None, max_number:int=None, min_number:int=None,\
        max_length:int=None, min_length:int=None, other_option:bool=None, vetical_alignment:bool=None,\
        alphabetical_order:bool=None, placeholder:str=None):
        
        pass
    
    @abstractmethod
    def create_settings(self, multiple_selection:bool=None, multiple_selection_scope:list[str]=None, choices:list[str]=None,\
        phone_number_choices:list[PhoneNumberFieldSettingsDTO]=None, max_number:int=None, min_number:int=None,\
        max_length:int=None, min_length:int=None, other_option:bool=None, vetical_alignment:bool=None,\
        alphabetical_order:bool=None, placeholder:str=None)->int:
        
        pass
    
    @abstractmethod
    def check_form_field(self, form_field_id:int):
        pass
    
    @abstractmethod
    def check_settings(self, id:int):
        pass
    
    @abstractmethod
    def add_settings_to_form_field(self, form_field_id:int, settings_id:int):
        pass
    
    @abstractmethod
    def check_if_invitation_expired(self, id:int):
        pass

    @abstractmethod
    def check_if_layout_is_valid_for_form(self, form_id:int, layout_id:int):
        pass

    @abstractmethod
    def create_or_update_layout_for_form(self, user_id:str, form_id:int, layout_name:str, layout_id:int)->int:
        pass

    @abstractmethod
    def check_layout(self, id:int):
        pass

    @abstractmethod
    def check_tab(self, id:int):
        pass

    @abstractmethod
    def check_if_tab_already_exists_for_layout(self, layout_id:int, tab_type:str):
        pass
    
    @abstractmethod
    def add_section_to_tab(self, tab_id:int, section_config_dto:SectionConfigDTO):
        pass

    @abstractmethod
    def create_or_update_tab_for_layout_for_section_config(self, tab_dto:TabDTO)->int:
        pass

    @abstractmethod
    def check_if_form_fields_exists(self, form_fields:list[int]):
        pass

    @abstractmethod
    def check_if_form_fields_belong_to_form(self, form_fields:list[int], layout_id:int):
        pass

    @abstractmethod
    def get_tab_details(self, tab_id:int)->TabDTO:
        pass

    @abstractmethod
    def update_layout_for_form(self, layout_id:int, layout_name:str):
        pass

    @abstractmethod
    def update_tab_for_section_config(self, tab_id:int, tab_name:str):
        pass

    @abstractmethod
    def check_if_form_field_ids_exists(form_field_ids:list[int]):
        pass

    @abstractmethod
    def create_or_update_tab_for_form_field_ids_config(self, tab_dto:TabDTO):
        pass

    @abstractmethod
    def add_form_field_ids_to_tab(self, tab_id:int, form_field_ids_config:FormFieldIdsConfigDTO):
        pass