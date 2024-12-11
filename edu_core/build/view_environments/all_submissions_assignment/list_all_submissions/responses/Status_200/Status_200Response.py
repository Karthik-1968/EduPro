class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"submitted_by": "string", "submitted_at": "2099-12-31 00:00:00", "Grade": "A", "remarks": "string"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from edu_core.build.view_environments.all_submissions_assignment.list_all_submissions.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass