class Status201Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"label": "string", "field_type": "Text", "place_holder": "string"}]',
            "response_serializer": "Status_201Serializer",
            "response_serializer_import_str": "from type_form.build.view_environments.add_fields_to_form_.add_fields_to_form.responses.Status_201.Status_201.Status_201Serializer import Status_201Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass