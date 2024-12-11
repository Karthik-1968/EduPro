class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"name": "string", "fee": 1.1, "duration": "string"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from edu_core.build.view_environments.all_courses.list_all_courses.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass