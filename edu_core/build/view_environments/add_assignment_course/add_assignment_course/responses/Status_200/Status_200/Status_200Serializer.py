from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class Status_200Type(object):
    def __init__(self, course=None, assignment=None, max_duration_in_minutes=None, assignment_description=None,  **kwargs):
        self.course = course
        self.assignment = assignment
        self.max_duration_in_minutes = max_duration_in_minutes
        self.assignment_description = assignment_description

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_200Serializer(serializers.Serializer):
    course = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    assignment = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    max_duration_in_minutes = serializers.FloatField(required=False, allow_null=True)
    assignment_description = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Status_200Type(**validated_data)
