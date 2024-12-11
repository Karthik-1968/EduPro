class LimitParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "Getlimit",
            "parameter_field_name": "limit"
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
        return serializers.IntegerField(required=False, allow_null=True, help_text="Some description for limit")
        

    @staticmethod
    def get_url_regex():
        pass