import pandas as pd
from type_form.models import Tab
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.presenters.presenter_implementation import PresenterImplementation
from type_form.interactors.storage_interfaces.storage_interface import TabDTO, SectionConfigDTO
import csv
import os

tab_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Tabs.csv'
df_tab = pd.read_csv(tab_csv_file_path)

print("----------------------------->", df_tab.columns)

storage = StorageImplementation()
presenter = PresenterImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)
    
for index, row in df_tab.iterrows():

    try:
        storage.check_form(id=row['form_id'])
    except Exception as e:
        print(e)

    try:
        storage.check_if_layout_already_exists_for_form(form_id=row['form_id'])
    except Exception as e:
        print(e)
    else:
        form_layout_interactor.create_layout_for_form(id=row['form_id'], user_id=row['user_id'], form_id=row['form_id'], \
        layout_name=row['layout_name'])

    try:
        storage.check_if_tab_already_exists_for_layout(layout_id=row['layout_id'], tab_type=row['tab_type'])
    except Exception as e:
        print(e)
    else:
        tab_dto = TabDTO(user_id=row['user_id'], layout_id=row['layout_id'], tab_type=row['tab_type'], tab_name=row['tab_name'])
        form_layout_interactor.create_tab_for_layout_for_section_config(tab_dto)
    
    section_config_dto = SectionConfigDTO(section_type=row['section_type'], section_name=row['section_name'], gof=row['gof_name'], \
                                          formfields=row['formfield_ids'])
    try:
        form_layout_interactor.add_section_to_tab(tab_id=row['tab_id'], sectionconfig_dto=section_config_dto)
    except Exception as e:
        print(str(e))