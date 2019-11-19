# from pyramid.view import view_config
# import pycharm_app.static_cache


# @view_config(route_name='index', renderer='templates/index.pt')
# def index(_):
#     albums = [
#         {'has_preview': True, 'title': 'song_name_here', 'url': 'album/123'},
#         {'has_preview': False, 'title': 'song_name_here2', 'url': 'album/124'}
#     ]
#     return extend_model({'project': 'pycharm_app',
#                          'albums': albums
#                          })


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def index(_):
#     return extend_model({'project': 'pycharm_app'})


# @view_config(route_name='box', renderer='templates/box_model.pt')
# def box_model(_):
#     return extend_model({})


# @view_config(route_name='selectors', renderer='templates/selectors.pt')
# def selectors(_):
#     return extend_model({})


# @view_config(route_name='layout', renderer='templates/layout.pt')
# def layout(_):
#     return extend_model({})


# @view_config(route_name='float', renderer='templates/float.pt')
# def float_(_):
#     return extend_model({})


# @view_config(route_name='reset_post', request_method='POST', renderer='templates/reset_password.jinja2')
# def reset_password(request):
#     # Collect data from route, querystring, POST etc.
#     email = request.POST.get('email')
#
#     # Process request
#     if not repository.create_reset_password(email):
#         return {'error': "Cannot reset password"}
#
#     # Return model to template engine
#     return {
#             'error': None,
#             'msg': 'Check your email for reset code'
#            }


# def extend_model(model_dict):
#     model_dict['build_cache_id'] = pycharm_app.static_cache.build_cache_id
#     return model_dict