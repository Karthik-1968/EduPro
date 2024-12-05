from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class BasicTodoType(object):
    def __init__(self, description, is_completed=None, remind_at=None,  **kwargs):
        self.description = description
        self.is_completed = is_completed
        self.remind_at = remind_at

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class BasicTodoSerializer(serializers.Serializer):
    description = serializers.CharField()
    is_completed = serializers.NullBooleanField(required=False)
    remind_at = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return BasicTodoType(**validated_data)
