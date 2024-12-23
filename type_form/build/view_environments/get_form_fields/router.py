path_method_dict = {
    "get/form/fields/": {
        "GET": "get_form_fields"
    }
}


def get_form_fields(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("type_form", "get_form_fields", operations_dict, request, *args, **kwargs)
    return response