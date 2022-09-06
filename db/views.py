from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from db.models import Maker
from django.views.generic.list import ListView # для отображения таблицы



class MakerView(ListView):
    models = Maker
    template_name = 'db_table/index.html'
    context_object_name = 'maker'

def index(request):
    return render(request, 'db_table/index.html')  # передаем через контекст

