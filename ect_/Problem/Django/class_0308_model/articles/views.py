from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # DB의 데이터를 모두 가져오는 방법
    # 모델을 이용해 모든 데이터 가져온다.
    # articles = Article.objects.all()[::-1]    # 데이터를 가져 와서 정렬한다.
    articles = Article.objects.order_by('-pk')  # 데이터를 가져올 때 부터 정렬한다. 내림차순은 - 붙여준다.

    # 가져온 데이터를 템플릿으로 넘긴다
    context = {
        'articles' : articles,
    }
    # 템플릿에서 데이터를 보여준다.
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title_get = request.POST.get('title')
    content_get = request.POST.get('content')
    Article.objects.create(title=title_get, content=content_get)

    return redirect('articles:index')   # 바로 인덱스로 page로 가고 싶다면 render 로 불러오는게 아닌 redirect로 직접 간다.
                                        # render로 불러 온다면 article 불러오는 문구를 한번 더 써줘야 된다.