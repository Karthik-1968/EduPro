class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"description": "string", "is_completed": true, "remind_at": "string", "id": 1}',
            "response_serializer": "TodoSerializer",
            "response_serializer_import_str": "from edu_core.build.serializers.definitions.Todo.TodoSerializer import TodoSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass