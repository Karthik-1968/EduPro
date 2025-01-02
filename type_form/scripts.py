from django.db import connection

def user():
   def table_exists(type_form_formresponse):
      with connection.cursor() as cursor:
         tables = connection.introspection.table_names(cursor)
         print(tables)
         return type_form_formresponse in tables
   if table_exists("type_form_formresponse"):
      print("Table exists!")
   else:
      print("Table does not exist.")