class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"description": "string", "is_completed": true, "remind_at": "string", "id": 1}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from edu_core.build.view_environments.todos_.get_todos.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass