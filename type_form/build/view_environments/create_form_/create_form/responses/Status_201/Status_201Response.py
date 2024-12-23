class Status201Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"form_id": 1}',
            "response_serializer": "Status_201Serializer",
            "response_serializer_import_str": "from type_form.build.view_environments.create_form_.create_form.responses.Status_201.Status_201.Status_201Serializer import Status_201Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass