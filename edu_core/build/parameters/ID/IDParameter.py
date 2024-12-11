class SearchParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "ID",
            "parameter_field_name": "search"
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
        return serializers.IntegerField(required=False, allow_null=True, help_text="Some description for name")
        

    @staticmethod
    def get_url_regex():
        pass