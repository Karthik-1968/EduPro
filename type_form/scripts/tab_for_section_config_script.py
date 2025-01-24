import pandas as pd
import uuid
from type_form.models import Tab
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.presenters.presenter_implementation import PresenterImplementation
from type_form.interactors.storage_interfaces.storage_interface import TabDTO, SectionConfigDTO
from type_form.exceptions import custom_exceptions
from schema import Schema, And, Use, SchemaError

tab_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Tabs.csv'
df_tab = pd.read_csv(tab_csv_file_path)

storage = StorageImplementation()
presenter = PresenterImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)

tab_status_csv_file_path = 'tab_status.csv'
tab_status = []
tab_gof_schema = Schema(
    {
        "user_id": And(Use(str), lambda s: isinstance(uuid.UUID(s), uuid.UUID)),
        "layout_id": And(Use(int), lambda n: n > 0),
        "tab_id": And(Use(int), lambda n: n > 0),
        "tab_type": And(str, len),
        "tab_name": And(str, len),
        "section_type": And(str, len),
        "gof_name": And(str, len)
    })

tab_formfield_ids_schema = Schema(
    {
        "user_id": And(Use(str), lambda s: isinstance(uuid.UUID(s), uuid.UUID)),
        "layout_id": And(Use(int), lambda n: n > 0),
        "tab_id": And(Use(int), lambda n: n > 0),
        "tab_type": And(str, len),
        "tab_name": And(str, len),
        "section_type": And(str, len),
        "section_name": And(str, len),
        "formfield_ids": And(list, lambda l: all(isinstance(i, int) for i in l), lambda l: all(i > 0 for i in l))
    })

def validate_tab_data_for_gof_section(tab_data_for_gof_section):
    try:
        tab_gof_schema.validate(tab_data_for_gof_section)
        return True, ""
    except SchemaError as e:
        return False, str(e)
def validate_tab_data_for_formfield_ids(tab_data_for_formfield_ids):
    try:
        tab_gof_schema.validate(tab_data_for_formfield_ids)
        return True, ""
    except SchemaError as e:
        return False, str(e)

for index, row in df_tab.iterrows():
    if row["section_type"] == "gof":
        tab_data_for_gof_section = {
            "user_id": row['user_id'],
            "layout_id": row['layout_id'],
            "tab_id": row['tab_id'],
            "tab_type": row['tab_type'],
            "tab_name": row['tab_name'],
            "section_type": row['section_type'],
            "gof_name": row['gof_name']
        }
        is_valid, error_message = validate_tab_data_for_gof_section(tab_data_for_gof_section)
    elif row["section_type"] == "formfield_ids":
        tab_data_for_formfield_ids = {
            "user_id": row['user_id'],
            "layout_id": row['layout_id'],
            "tab_id": row['tab_id'],
            "tab_type": row['tab_type'],
            "tab_name": row['tab_name'],
            "section_type": row['section_type'],
            "section_name": row['section_name'],
            "formfield_ids": row['formfield_ids']
        }
        is_valid, error_message = validate_tab_data_for_formfield_ids(tab_data_for_formfield_ids)
    
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
    
    row["status"] = status
    row["remarks"] = remarks
    tab_status.append(row)

df_tab_status = pd.DataFrame(tab_status)
df_tab_status.to_csv(tab_status_csv_file_path, index=False)
