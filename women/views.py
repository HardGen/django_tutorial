from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [
    {'title': "О Сайте", 'url_name': 'about'},
    {'title': "Добавить Статью", 'url_name': 'add_page'},
    {'title': "Обратая Связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]
# Create your views here.
def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная Страница',
        'cat_selected': 0
    }

    return render(request,'women/index.html',context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О Сайте'})


def login(request):
    return HttpResponse("Авторизация")

    
def contact(request):
    return HttpResponse("Обратная связь")

def addpage(request):
    return HttpResponse("Добавление статьи")

def show_post(response, post_id):
    return HttpResponse(f"PST={post_id}")

def pageNotFound(reques, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    
    if len(posts) == 0:
        raise Http404()
        
    context = {
        'posts': posts,
        'menu': menu,
        'title': "Отображение по рубриками",
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', context=context)