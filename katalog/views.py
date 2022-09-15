from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Alifia Nadiya Putri',
        'npm': '2106708002',
    }
    return render(request, "katalog.html", context)