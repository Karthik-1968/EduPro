from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class adding_assignment_courseType(object):
    def __init__(self, assignment_id, course_id,  **kwargs):
        self.assignment_id = assignment_id
        self.course_id = course_id

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class adding_assignment_courseSerializer(serializers.Serializer):
    assignment_id = serializers.IntegerField()
    course_id = serializers.IntegerField()

    def create(self, validated_data):
        return adding_assignment_courseType(**validated_data)
