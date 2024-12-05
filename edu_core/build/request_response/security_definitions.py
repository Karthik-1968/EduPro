from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from dsu.dsu_gen.openapi.utils.is_valid_api_key import IsValidAPIKey

SECURITY_DEFINITIONS = {

    "oauth" : {
        "TYPE": "OAUTH2",
        "AUTHENTICATION_CLASSES": [OAuth2Authentication],
        "PERMISSIONS_REQUIRED": [IsAuthenticated],
        "SCOPES_REQUIRED": ["read", "write", "update", "delete"]
    }
}