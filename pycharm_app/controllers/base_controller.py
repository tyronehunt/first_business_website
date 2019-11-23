import pycharm_app.infrastructure.static_cache as static_cache
import pyramid.renderers
import pyramid.httpexceptions as exc
from pycharm_app.infrastructure.suppressor import suppress


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id
        self.page_title = "My web app"

        # Make _layout.pt available to all renderers
        layout_render = pyramid.renderers.get_renderer('pycharm_app:templates/shared/_layout.pt')
        impl = layout_render.implementation()
        self.layout = impl.macros['layout']

    @property
    def is_logged_in(self):
        return False

    # noinspection PyMethodMayBeStatic
    def redirect(self, to_url, permanent=False):
        if permanent:
            raise exc.HTTPMovedPermanently(to_url)
        raise exc.HTTPFound(to_url)


    # @suppress
    # def dont_expose_web_action_base(self):
    #     print("Called don't expose as web action, what happened")
    #
    # @property
    # def is_get(self):
    #     return self.request.method == 'GET'
    #
    # @property
    # def is_get(self):
    #     return self.request.method == 'POST'

    def set_title(self, page_title):
        self.page_title = "{} - [{}]".format(
            page_title, BaseController.page_title)
