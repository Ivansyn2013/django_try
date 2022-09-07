from db.models import Maker


# настройка переадресации на другую бд
class MyDBRouter:

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == Maker:
            return 'med_db'
        return None
