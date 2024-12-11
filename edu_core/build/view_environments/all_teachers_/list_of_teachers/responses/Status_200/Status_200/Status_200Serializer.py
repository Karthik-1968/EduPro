from rest_framework import serializers
from edu_core.build.serializers.definitions.user.userSerializer import userSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = userSerializer()
