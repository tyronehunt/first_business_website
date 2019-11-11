from pyramid.view import view_config
import my_pycharm_app.utils

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'my_pycharm_app'}

def extend_model(model_dict):
    model_dict['build_cache_id'] = my_pycharm_app.utils.build_cache_id
    return model_dict