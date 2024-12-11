from rest_framework import serializers
from edu_core.build.serializers.definitions.course.courseSerializer import courseSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = courseSerializer()
