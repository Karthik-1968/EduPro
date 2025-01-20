import pandas as pd
from type_form.models import Layout
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.presenters.presenter_implementation import PresenterImplementation
from type_form.exceptions import custom_exceptions

layout_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Layout.csv'
df_layout = pd.read_csv(layout_csv_file_path)

storage = StorageImplementation()
presenter = PresenterImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)

layout_status_csv_file_path = 'layout_status.csv'
layout_status = []

for index, row in df_layout.iterrows():
    try:
        form_layout_interactor.create_or_update_layout_for_form(user_id=row['user_id'], form_id=row['form_id'], layout_name=row['layout_name'], \
                                                                layout_id=row['layout_id'])
        status = "Created"
        remarks = "Layout created successfully"
    except custom_exceptions.InvalidFormException as e:
        status = "Failed"
        remarks = str(e)
    except custom_exceptions.InvalidLayoutForFormException as e:
        status = "Failed"
        remarks = str(e)
    except Exception as e:
        status = "Failed"
        remarks = str(e)
    
    layout_status.append({"form_id":row['form_id'], "user_id":row['user_id'], "layout_id":row['layout_id'], "layout_name":row['layout_name'], \
                    "status":status, "remarks":remarks})

df_layout_status = pd.DataFrame(layout_status)

df_layout_status.to_csv(layout_status_csv_file_path, index=False)