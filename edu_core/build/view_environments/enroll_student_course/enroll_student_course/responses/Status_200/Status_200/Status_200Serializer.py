from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class Status_200Type(object):
    def __init__(self, student=None, course=None, fee=None, duration=None,  **kwargs):
        self.student = student
        self.course = course
        self.fee = fee
        self.duration = duration

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_200Serializer(serializers.Serializer):
    student = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    course = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    fee = serializers.FloatField(required=False, allow_null=True)
    duration = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Status_200Type(**validated_data)
