class IdParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "TodoId",
            "parameter_field_name": "id"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        pass

    @staticmethod
    def get_serializer_field():
        from rest_framework import serializers
        from dsu.dsu_gen.openapi.fields.collection_format_field import \
            CollectionFormatField
        return serializers.IntegerField(help_text="todo id")
        

    @staticmethod
    def get_url_regex():
        regex = r"(?P<id>\d+)"
        return regex