from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
from multiprocessing import context
from mywatchlist.models import MyWatchList

# TODO: Create your views here.
def show_mywatchlist(req):
    data_mywatchlist = MyWatchList.objects.all()
    ctx = {
        'list_mywatchlist':  data_mywatchlist,
        'nama': 'Raudhatul Jannah',
        'id'  : '2106654422'

    }

    return render(req, "mywatchlist.html", ctx)

def show_xml(req):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(req):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_html(req):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("html", data_mywatchlist), content_type="application/html")