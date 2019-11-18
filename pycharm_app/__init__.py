from pyramid.config import Configurator
import pycharm_app.controllers.home_controller as home


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')

    # Set up the static folder
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Set up the template folder routes
    config.add_route('index', '/')
    config.add_route('box', '/box-model')
    config.add_route('selectors', '/selectors')
    config.add_route('layout', '/layout')
    config.add_route('float', '/float')

    # Reference other integrations
    cfg_settings = config.get_settings()
    db_file = cfg_settings.get('db_file')
    api_key = cfg_settings.get('api_key')
    config.scan()

    # Add handlers
    config.add_handler('home_action_id', '/home/{action}/{id}', handler=home.HomeController)


    return config.make_wsgi_app()