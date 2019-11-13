from pyramid.view import view_config
import pycharm_app.static_cache


@view_config(route_name='mytemplate', renderer='templates/mytemplate.pt')
def index(_):
    return extend_model({'project': 'pycharm_app'})


@view_config(route_name='layout', renderer='templates/layout.pt')
def layout(_):
    return extend_model({'project': 'pycharm_app'})


def extend_model(model_dict):
    print("extend_model called on", model_dict)
    model_dict['build_cache_id'] = pycharm_app.static_cache.build_cache_id
    print("model_dict returned as:", model_dict)
    return model_dict

extend_model({'project': 'pycharm_app'})