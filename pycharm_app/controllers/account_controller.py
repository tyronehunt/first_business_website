import pyramid_handlers
from pycharm_app.controllers.base_controller import BaseController


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/accounts/index.pt')
    def index(self):
        return {}