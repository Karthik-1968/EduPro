import pandas as pd 
from type_form.models import User
from type_form.interactors.user_interactor import UserInteractor
from type_form.storages.storage_implementation import StorageImplementation
from type_form.presenters.presenter_implementation import PresenterImplementation
import csv
import os

user_csv_file_path = 'https://raw.githubusercontent.com/dayanakarthik-2011/EduPro/refs/heads/dev1/Type_form.csv'
status_csv_file_path = 'status_file.csv'
df_user = pd.read_csv(user_csv_file_path)

storage = StorageImplementation()
presenter = PresenterImplementation()
user_interactor = UserInteractor(storage = storage)

status_data = []

for index, row in df_user.iterrows():
    user_id = row['id']
    email = row['email']

    USER_ALREADY_PRESENT = "User already present"

    try:
        user_interactor.create_user(id=user_id, email=email, presenter=presenter)

        user_status = "Created"
    except Exception as e:
        response = str(e)
        if "User already present" in response:
            print(f"Error: {USER_ALREADY_PRESENT}")
            user_status = "Created"
        else:
            print(f"Unexpected error occurred: {response}")
            user_status = "Failed"

    status_data.append({"id": user_id, "email": email, "status": user_status})

df_status = pd.DataFrame(status_data)

df_status.to_csv(status_csv_file_path, index=False)

if os.path.exists(status_csv_file_path):
    print(f"File successfully created: {status_csv_file_path}")
else:
    print("Failed to create the status file.")