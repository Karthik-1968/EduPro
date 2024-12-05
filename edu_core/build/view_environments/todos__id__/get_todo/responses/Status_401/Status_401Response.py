class Status401Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"response": "string", "http_status_code": 1, "res_status": "DUPLICATE_TO_IDS"}',
            "response_serializer": "DefaultHttpExceptionFieldsSerializer",
            "response_serializer_import_str": "from edu_core.build.serializers.definitions.DefaultHttpExceptionFields.DefaultHttpExceptionFieldsSerializer import DefaultHttpExceptionFieldsSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass