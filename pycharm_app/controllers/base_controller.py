import pycharm_app.infrastructure.static_cache as static_cache
from pycharm_app.infrastructure.suppressor import suppress


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id
        self.page_title = "My web app"

    @suppress
    def dont_expose_web_action_base(self):
        print("Called don't expose as web action, what happened")

    @property
    def is_get(self):
        return self.request.method == 'GET'

    @property
    def is_get(self):
        return self.request.method == 'POST'

    def set_title(self, page_title):
        self.page_title = "{} - [{}]".format(
            page_title, BaseController.page_title)
