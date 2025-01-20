import pandas as pd
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

for index, row in df_tab.iterrows():

    try:
        tab_dto = TabDTO(tab_id=row['tab_id'], user_id=row['user_id'], layout_id=row['layout_id'], tab_type=row['tab_type'],\
                             tab_name=row['tab_name'])
        form_layout_interactor.create_or_update_tab_for_layout_for_section_config(tab_dto=tab_dto)

        section_config_dto = SectionConfigDTO(section_type=row['section_type'], section_name=row['section_name'], gof=row['gof_name'], \
                                              formfields=row['formfield_ids'])

        form_layout_interactor.add_section_to_tab(tab_id=row['tab_id'], sectionconfig_dto=section_config_dto)

        status = "Added"
        remarks = "Section added to tab successfully"
    except custom_exceptions.InvalidLayoutException as e:
        status = "Failed"
        remarks = str(e)
    except Exception as e:
        status = "Failed"
        remarks = str(e)

    tab_status.append({"user_id":row['user_id'], "layout_id":row['layout_id'], "tab_id":row['tab_id'], "tab_type":row['tab_type'], \
                    "tab_name":row['tab_name'], "section_type":row['section_type'], "section_name":row['section_name'], \
                        "gof_name":row['gof_name'], "formfield_ids":row['formfield_ids'], "status":status, "remarks":remarks})

df_tab_status = pd.DataFrame(tab_status)

df_tab_status.to_csv(tab_status_csv_file_path, index=False)