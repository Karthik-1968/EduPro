import pandas as pd
from type_form.interactors.form_layout_interactor import FormLayoutInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.interactors.storage_interfaces.storage_interface import ColumnDTO, CellDTO, RowDTO, TableDTO
from type_form.exceptions import custom_exceptions

tab_for_column_table_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/ColTable.csv'
tab_for_table_config_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/TableTab.csv'
df_tab_for_table_config = pd.read_csv(tab_for_column_table_csv_file_path)
df_tab_for_table_config = pd.read_csv(tab_for_table_config_csv_file_path)
tab_id = 2

storage = StorageImplementation()
form_layout_interactor = FormLayoutInteractor(storage=storage)

columns = []
for index, row in df_tab_for_table_config.iterrows():
    columns.append(ColumnDTO(column_name=row['column_name'], show_as_label=row['show_as_label'], user_should_fill_response=\
                             row['user_should_fill_response']))

rows = []
for index, row in df_tab_for_table_config.iterrows():
    cells = []
    for column in columns:
        cells.append(CellDTO(column_name=column.column_name, field_id=row[column.column_name]))
    rows.append(RowDTO(row_name=row['row_name'], cells=cells))

table_dto = TableDTO(rows=rows, columns=columns)

try:
    form_layout_interactor.add_table_config_to_tab(tab_id=tab_id, table_dto=table_dto)
except custom_exceptions.InvalidTabException as e:
    print(str(e))
except Exception as e:
    print(str(e))