from db.models import Maker, Introducer


# настройка переадресации на другую бд
class MyDBRouter:

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == Maker:
            return 'med_db'
        elif model == Introducer:
            return 'med_db'
        else:
            return None
