from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class formType(object):
    def __init__(self, name=None, created_by=None,  **kwargs):
        self.name = name
        self.created_by = created_by

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class formSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    created_by = serializers.EmailField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return formType(**validated_data)
