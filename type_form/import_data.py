import pandas as pd 
from type_form.models import User

csv_file_path = "C:\Users\91934\OneDrive\Type_form.csv"
df = pd.read_csv(csv_file_path)

for index, row in df.iterrows():
    User.objects.create(id=row['id'], email=row['email'])