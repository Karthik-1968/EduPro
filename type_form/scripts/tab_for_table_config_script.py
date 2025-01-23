import pandas as pd
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.interactors.storage_interfaces.storage_interface import MatrixConfigDTO
from type_form.exceptions import custom_exceptions

tab_for_table_config_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Tabs.csv'
df_tab_for_table_config = pd.read_csv(tab_for_table_config_csv_file_path)
tab_id = 2
non_editable = ["Name"]
editable = ["Age", "Phonenumber", "Feedback"]

user_response = {}

storage = StorageImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)

columns = []

for column_name in df_tab_for_table_config.columns:
    if column_name in non_editable:
        columns.append(ColumnDTO(column_name=column_name, show_as_label=True, user_should_fill_response=False))
    elif column_name in editable:
        columns.append(ColumnDTO(column_name=column_name, show_as_label=True, user_should_fill_response=True))

rows = []
for index, row in df_tab_for_table_config.iterrows():
    row_name = f"Row{index + 1}"
    
    cells = []
    for column_name in df_tab_for_table_config.columns:
        field_id = f"{column_name.lower()}_{row_name.lower().replace(' ', '_')}_display"
        cells.append(CellDTO(column_name=column_name, field_id=field_id))
        user_response[field_id] = row[column_name]
    
    rows.append(RowDTO(row_name=row_name, cells=cells))

table_dto = TableDTO(rows=rows, columns=columns)

try:
    form_layout_interactor.create_or_update_matrix_config_for_tab(tab_id=tab_id, table_dto=table_dto, user_response=user_response)
except custom_exceptions.InvalidTabException as e:
    print(str(e))
except Exception as e:
    print(str(e))