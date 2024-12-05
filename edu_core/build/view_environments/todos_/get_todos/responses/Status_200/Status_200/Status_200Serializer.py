from rest_framework import serializers
from edu_core.build.serializers.definitions.Todo.TodoSerializer import TodoSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = TodoSerializer()
