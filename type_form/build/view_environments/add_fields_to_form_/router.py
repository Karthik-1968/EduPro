path_method_dict = {
    "add/fields/to/form/": {
        "POST": "add_fields_to_form"
    }
}


def add_fields_to_form_(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("type_form", "add_fields_to_form_", operations_dict, request, *args, **kwargs)
    return response