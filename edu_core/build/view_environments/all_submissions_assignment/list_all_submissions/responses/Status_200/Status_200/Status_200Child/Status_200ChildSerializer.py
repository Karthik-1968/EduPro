from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class Status_200ChildType(object):
    def __init__(self, submitted_by=None, submitted_at=None, Grade=None, remarks=None,  **kwargs):
        self.submitted_by = submitted_by
        self.submitted_at = submitted_at
        self.Grade = Grade
        self.remarks = remarks

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_200ChildSerializer(serializers.Serializer):
    submitted_by = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    submitted_at = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')
    Grade = serializers.ChoiceField(choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), required=False, allow_blank=True, allow_null=True)
    remarks = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Status_200ChildType(**validated_data)
