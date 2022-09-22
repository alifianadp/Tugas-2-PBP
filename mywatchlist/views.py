from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    count_watched = 0
    for title in data_mywatchlist:
        if(title.watched=="Yes"):
            count_watched+=1
    if(count_watched > 10 - count_watched):
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan  = "Wah, kamu masih sedikit menonton!"
    context = {
        'list_watch': data_mywatchlist,
        'nama': 'Alifia Nadiya Putri',
        'npm': '2106708002',
        'pesan': pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")