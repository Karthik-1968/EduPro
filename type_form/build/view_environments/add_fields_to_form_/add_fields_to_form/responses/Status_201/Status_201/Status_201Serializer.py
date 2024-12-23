from rest_framework import serializers
from type_form.build.view_environments.add_fields_to_form_.add_fields_to_form.responses.Status_201.Status_201.Status_201Child.Status_201ChildSerializer import Status_201ChildSerializer

class Status_201Serializer(serializers.ListSerializer):
    child = Status_201ChildSerializer()
