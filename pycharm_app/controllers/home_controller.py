import pyramid_handlers


class HomeController():


    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'data': data}


    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'data': data}