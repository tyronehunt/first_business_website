import pyramid_handlers
from pycharm_app.controllers.base_controller import BaseController
from pycharm_app.services.albums_service import AlbumsService


class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer='templates/albums/index.pt')
    def index(self):
        # data / service access
        all_albums = AlbumsService.get_albums()

        # return the model
        return {'albums': all_albums}
