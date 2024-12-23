from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class DataType(object):
    def __init__(self, field_id=None, response=None,  **kwargs):
        self.field_id = field_id
        self.response = response

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class DataSerializer(serializers.Serializer):
    field_id = serializers.IntegerField(required=False, allow_null=True)
    response = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return DataType(**validated_data)
