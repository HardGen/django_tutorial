from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return HttpResponse("Страница приложении Women")


def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категории</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2028:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Статьи по категории</h1><p>{year}</p>")


def pageNotFound(reques, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')