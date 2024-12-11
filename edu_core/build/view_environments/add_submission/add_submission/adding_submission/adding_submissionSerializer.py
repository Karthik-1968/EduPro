from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class adding_submissionType(object):
    def __init__(self, student_id=None, assignment_id=None, submitted_at=None,  **kwargs):
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.submitted_at = submitted_at

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class adding_submissionSerializer(serializers.Serializer):
    student_id = serializers.IntegerField(required=False, allow_null=True)
    assignment_id = serializers.IntegerField(required=False, allow_null=True)
    submitted_at = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return adding_submissionType(**validated_data)
