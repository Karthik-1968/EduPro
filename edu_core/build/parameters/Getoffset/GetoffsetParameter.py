class OffsetParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "Getoffset",
            "parameter_field_name": "offset"
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
        return serializers.IntegerField(required=False, allow_null=True, help_text="Some description for offset")
        

    @staticmethod
    def get_url_regex():
        pass