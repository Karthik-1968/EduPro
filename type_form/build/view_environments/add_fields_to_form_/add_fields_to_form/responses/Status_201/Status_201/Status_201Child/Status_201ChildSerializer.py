from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class Status_201ChildType(object):
    def __init__(self, label, field_type, place_holder=None,  **kwargs):
        self.label = label
        self.field_type = field_type
        self.place_holder = place_holder

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Status_201ChildSerializer(serializers.Serializer):
    label = serializers.CharField()
    field_type = serializers.ChoiceField(choices=(('Text', 'Text'), ('Integer', 'Integer'), ('Float', 'Float'), ('Email', 'Email'), ('Decimal', 'Decimal'), ('Boolean', 'Boolean'), ('DateTime', 'DateTime'), ('UUID', 'UUID'), ('Binary', 'Binary'), ('Date', 'Date'), ('Time', 'Time'), ('JSON', 'JSON'), ('PhoneNumber', 'PhoneNumber')))
    place_holder = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Status_201ChildType(**validated_data)
