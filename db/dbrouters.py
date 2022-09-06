from models import Maker


# настройка переадресации на другую бд
class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == Maker:
            return 'med_db'
        return None
