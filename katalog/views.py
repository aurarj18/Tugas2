from django.shortcuts import render

# TODO: Create your views here.
from multiprocessing import context
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(req):
    data_katalog = CatalogItem.objects.all()
    ctx = {
        'list_katalog':  data_katalog,
        'nama': 'Raudhatul Jannah',
        'id'  : '2106654422'

    }

    return render(req, "katalog.html", ctx)
