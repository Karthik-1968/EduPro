from rest_framework import serializers
from type_form.build.view_environments.get_form_fields.get_form_fields.responses.Status_200.Status_200.Status_200Child.Status_200ChildSerializer import Status_200ChildSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = Status_200ChildSerializer()
