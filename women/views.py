from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = ["О Сайте","Добавить Статью","Обратая Связь","Войти"]

# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(
        request,
        'women/index.html',
        {
            'posts': posts,
            'menu': menu,
            'title': 'Главная Страница'
        }
        )

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О Сайте'})


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