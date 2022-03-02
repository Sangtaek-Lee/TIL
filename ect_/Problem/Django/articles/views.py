from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# def index(request):
#     return HttpResponse('<h1>Hola</h1>')

def index(request):
    return render(request, 'articles/index.html')


# def greeting(request):
#     return render(request, 'greeting.html', {'name':'Alice',})
def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name' : 'Alice',
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/greeting.html', context)
