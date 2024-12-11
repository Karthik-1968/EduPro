from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class ListOfStudentsRequestQueryParamType(object):
    def __init__(self, limit=None, offset=None, search=None,  **kwargs):
        self.limit = limit
        self.offset = offset
        self.search = search

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class ListOfStudentsRequestQueryParamSerializer(serializers.Serializer):
    limit = serializers.IntegerField(required=False, allow_null=True, help_text="Some description for limit")
    offset = serializers.IntegerField(required=False, allow_null=True, help_text="Some description for offset")
    search = serializers.IntegerField(required=False, allow_null=True, help_text="Some description for name")

    def create(self, validated_data):
        return ListOfStudentsRequestQueryParamType(**validated_data)
