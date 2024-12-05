class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"id": 1}',
            "response_serializer": "TodoIdSerializer",
            "response_serializer_import_str": "from edu_core.build.serializers.definitions.TodoId.TodoIdSerializer import TodoIdSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass