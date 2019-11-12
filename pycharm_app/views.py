from pyramid.view import view_config
import pycharm_app.utils


@view_config(route_name='index', renderer='templates/mytemplate.pt')
def index(_):
    return extend_model({'project': 'pycharm_app'})


@view_config(route_name='layout', renderer='templates/layout.pt')
def layout(_):
    return extend_model({})


def extend_model(model_dict):
    model_dict['build_cache_id'] = pycharm_app.utils.build_cache_id
    return model_dict
