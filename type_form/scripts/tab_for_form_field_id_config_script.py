import pandas as pd
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.interactors.storage_interfaces.storage_interface import TabDTO, FormFieldIdsConfigDTO
from type_form.exceptions import custom_exceptions

tab_for_form_field_ids_config_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Tabs.csv'
df_tab_for_form_field_ids_config = pd.read_csv(tab_for_form_field_ids_config_csv_file_path)

storage = StorageImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)

tab_for_form_field_ids_config_status_csv_file_path = 'tab_for_form_field_ids_config_status.csv'

tab_for_form_field_ids_config_status = []

for index, row in df_tab_for_form_field_ids_config.iterrows():
    try:
        tab_dto = TabDTO(user_id=row['user_id'], layout_id=row['layout_id'], tab_id=row['tab_id'], tab_name=row['tab_name'], \
                                tab_type=row['tab_type'])
        form_layout_interactor.create_or_update_tab_for_form_field_ids_config(tab_dto=tab_dto)

        form_field_ids_config_dto = FormFieldIdsConfigDTO(name=row['name'], dob=row['dob'], contact_information=\
                                    row['contact_information'], work_experience=row['work_experience'], signature=row['signature'], \
                                        date=row['date'])

        form_layout_interactor.add_form_field_ids_to_tab(tab_id=row['tab_id'], form_field_ids_config_dto=form_field_ids_config_dto)

        status = "Added"
        remarks = "Form field ids added to tab successfully"
    except custom_exceptions.InvalidUserException as e:
        status = "Failed"
        remarks = str(e)
    except custom_exceptions.InvalidLayoutException as e:
        status = "Failed"
        remarks = str(e)

    tab_for_form_field_ids_config_status.append({ 'user_id': row['user_id'], 'layout_id': row['layout_id'], 'tab_id': row['tab_id'], \
    'tab_name': row['tab_name'], 'tab_type': row['tab_type'], 'name': row['name'], 'dob': row['dob'], 'contact_information': \
    row['contact_information'], 'work_experience': row['work_experience'], 'signature': row['signature'], 'date': row['date'], \
    'status': status, 'remarks': remarks })       

df_tab_for_form_field_ids_config_status = pd.DataFrame(tab_for_form_field_ids_config_status)

df_tab_for_form_field_ids_config_status.to_csv(tab_for_form_field_ids_config_status_csv_file_path, index=False)
