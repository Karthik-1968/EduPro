from django.conf.urls import include
from django.urls import re_path

from type_form.build.view_environments.user_email_.router import user_email_
from type_form.build.view_environments.login_.router import login_
from type_form.build.view_environments.logout_.router import logout_
from type_form.build.view_environments.create_form_.router import create_form_
from type_form.build.view_environments.add_fields_to_form_.router import add_fields_to_form_
from type_form.build.view_environments.get_form_fields.router import get_form_fields
from type_form.build.view_environments.submit_data_.router import submit_data_


base_path = "api/ip_traffic/"

api_paths = [
    re_path(r'^user/email/$', user_email_),
    re_path(r'^login/$', login_),
    re_path(r'^logout/$', logout_),
    re_path(r'^create/form/$', create_form_),
    re_path(r'^add/fields/to/form/$', add_fields_to_form_),
    re_path(r'^get/form/fields/$', get_form_fields),
    re_path(r'^submit/data/$', submit_data_),
]


urlpatterns = [
    re_path(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
