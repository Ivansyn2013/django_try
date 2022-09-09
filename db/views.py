from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from db.models import Maker, Introducer
from django.views.generic.list import ListView  # для отображения таблицы
from django.db import connections


class MakerView(ListView):
    models = Maker
    template_name = 'db_table/index.html'
    context_object_name = 'maker'

#
# def index(request):
#     data = Introducer.objects.first()
#     filds_name = list(data.__dict__.keys())  # способ получить имена атрибутов класса
#
#     context = {
#         'maker': Maker.objects.all(),
#         'introducer': Introducer.objects.all(),
#         'fields_name': filds_name[1:],
#     }
#     return render(request, 'db_table/index.html', context)  # передаем через контекст


def join_table(request):
    data = Introducer.objects.first()
    filds_name = list(data.__dict__.keys())

    with connections['med_db'].cursor() as cursor:
        cursor.execute('SELECT * FROM maker JOIN introducer  ON maker.id=introducer.maker_id ;')
        result = cursor.fetchall()

    print('это резульат', result)
    context = {
        'fields_name': filds_name[1:],
        'join_table': result,
    }
    return render(request, 'db_table/index.html', context)
