import pandas as pd
import uuid
from type_form.models import Tab
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.presenters.presenter_implementation import PresenterImplementation
from type_form.interactors.storage_interfaces.storage_interface import TabDTO, SectionConfigDTO
from type_form.exceptions import custom_exceptions

tab_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Tabs.csv'
df_tab = pd.read_csv(tab_csv_file_path)

storage = StorageImplementation()
presenter = PresenterImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)

tab_status_csv_file_path = 'tab_status.csv'
tab_status = []

def validate_user_id(user_id):
    try:
        uuid.UUID(user_id)
        return True, ""
    except ValueError:
        return False, "User ID must be a valid UUID format."

def validate_layout_id(layout_id):
    try:
        layout_id = int(layout_id)
        if layout_id <= 0:
            return False, "Layout ID must be a positive integer."
        return True, ""
    except ValueError:
        return False, "Layout ID must be a valid integer."

def validate_tab_id(tab_id):
    try:
        tab_id = int(tab_id)
        if tab_id <= 0:
            return False, "Tab ID must be a positive integer."
        return True, ""
    except ValueError:
        return False, "Tab ID must be a valid integer."

def validate_tab_type(tab_type):
    if not isinstance(tab_type, str):
        return False, "Tab Type must be a string."
    if not tab_type.strip():
        return False, "Tab Type cannot be an empty string."
    return True, ""

def validate_tab_name(tab_name):
    if not isinstance(tab_name, str):
        return False, "Tab Name must be a string."
    if not tab_name.strip():
        return False, "Tab Name cannot be an empty string."
    return True, ""

def validate_section_type(section_type):
    if not isinstance(section_type, str):
        return False, "Section Type must be a string."
    if not section_type.strip():
        return False, "Section Type cannot be an empty string."
    return True, ""

def validate_section_name(section_name):
    if not isinstance(section_name, str):
        return False, "Section Name must be a string."
    if not section_name.strip():
        return False, "Section Name cannot be an empty string."
    return True, ""

def validate_gof_name(gof_name):
    if not isinstance(gof_name, str):
        return False, "GOF Name must be a string."
    if not gof_name.strip():
        return False, "GOF Name cannot be an empty string."
    return True, ""

def validate_formfield_ids(formfield_ids):
    try:
        evaluated_ids = eval(formfield_ids)

        if not isinstance(evaluated_ids, list):
            return False, "Formfield IDs must be a list."

        if not all(isinstance(i, int) for i in evaluated_ids):
            return False, "All elements in Formfield IDs must be integers."
        return True, ""
    
    except (SyntaxError, ValueError, TypeError, NameError):
        return False, "Formfield IDs must be a valid list in string format."

def validate_row(row):
    is_valid, error_message = validate_user_id(row['user_id'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_layout_id(row['layout_id'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_tab_id(row['tab_id'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_tab_type(row['tab_type'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_tab_name(row['tab_name'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_section_type(row['section_type'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_section_name(row['section_name'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_gof_name(row['gof_name'])
    if not is_valid:
        return False, error_message
    
    is_valid, error_message = validate_formfield_ids(row['formfield_ids'])
    if not is_valid:
        return False, error_message

    return True, ""
for index, row in df_tab.iterrows():
    is_valid, error_message = validate_row(row)
    
    if not is_valid:
        status = "Failed"
        remarks = error_message
    else:
        try:
            tab_dto = TabDTO(tab_id=row['tab_id'], user_id=row['user_id'], layout_id=row['layout_id'], tab_type=row['tab_type'], tab_name=row['tab_name'])
            form_layout_interactor.create_or_update_tab_for_layout_for_section_config(tab_dto=tab_dto)

            section_config_dto = SectionConfigDTO(section_type=row['section_type'], section_name=row['section_name'], gof=row['gof_name'], formfields=row['formfield_ids'])
            form_layout_interactor.add_section_to_tab(tab_id=row['tab_id'], sectionconfig_dto=section_config_dto)

            status = "Added"
            remarks = "Section added to tab successfully"
        except custom_exceptions.InvalidLayoutException as e:
            status = "Failed"
            remarks = str(e)
        except Exception as e:
            status = "Failed"
            remarks = str(e)
    
    tab_status.append({
        "user_id": row['user_id'],
        "layout_id": row['layout_id'],
        "tab_id": row['tab_id'],
        "tab_type": row['tab_type'],
        "tab_name": row['tab_name'],
        "section_type": row['section_type'],
        "section_name": row['section_name'],
        "gof_name": row['gof_name'],
        "formfield_ids": row['formfield_ids'],
        "status": status,
        "remarks": remarks
    })

df_tab_status = pd.DataFrame(tab_status)
df_tab_status.to_csv(tab_status_csv_file_path, index=False)
