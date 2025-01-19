from type_form.import_data import status_csv_file_path
import pandas as pd

def get_status_file():
      df_status = pd.read_csv(status_csv_file_path)
      print(df_status)