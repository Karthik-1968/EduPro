path_method_dict = {
    "delete/assignment/": {
        "DELETE": "delete_assignment"
    }
}


def delete_assignment(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("edu_core", "delete_assignment", operations_dict, request, *args, **kwargs)
    return response