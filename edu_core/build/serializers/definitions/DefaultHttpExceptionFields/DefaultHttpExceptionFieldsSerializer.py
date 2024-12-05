from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class DefaultHttpExceptionFieldsType(object):
    def __init__(self, response, http_status_code, res_status,  **kwargs):
        self.response = response
        self.http_status_code = http_status_code
        self.res_status = res_status

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class DefaultHttpExceptionFieldsSerializer(serializers.Serializer):
    response = serializers.CharField()
    http_status_code = serializers.IntegerField()
    res_status = serializers.ChoiceField(choices=(('DUPLICATE_TO_IDS', 'DUPLICATE_TO_IDS'), ('INVALID_INPUT_TO_IDS', 'INVALID_INPUT_TO_IDS')))

    def create(self, validated_data):
        return DefaultHttpExceptionFieldsType(**validated_data)
