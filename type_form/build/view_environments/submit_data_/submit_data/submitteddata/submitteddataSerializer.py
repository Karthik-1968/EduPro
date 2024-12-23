from rest_framework import serializers

from dsu.dsu_gen.openapi.decorator.deserialize import deserialize
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_object
from dsu.dsu_gen.openapi.utils.type_file_utils import get_type_list_object
from dsu.dsu_gen.openapi.fields.collection_format_field import CollectionFormatField


class submitteddataType(object):
    def __init__(self, form_id, data,  **kwargs):
        self.form_id = form_id
        self.data = data

    def __str__(self):
        from dsu.dsu_gen.openapi.utils.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class submitteddataSerializer(serializers.Serializer):
    form_id = serializers.IntegerField()
    from type_form.build.view_environments.submit_data_.submit_data.submitteddata.Data.DataSerializer import DataSerializer
    data = DataSerializer(many=True)

    def create(self, validated_data):
        from type_form.build.view_environments.submit_data_.submit_data.submitteddata.Data.DataSerializer import DataSerializer
        data_val = []
        data_list_val = validated_data.pop("data", [])
        for each_data in data_list_val:
            each_obj, _ = deserialize(DataSerializer, each_data, many=False, partial=True)
            data_val.append(each_obj)
        
        return submitteddataType(data=data_val, **validated_data)
