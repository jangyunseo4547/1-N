from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else:            # new 먼저 
        form = ArticleForm()

    context = {
        'form':form,
    }

    return render(request, 'create.html', context)


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def detail(request,id):
    article = Article.objects.get(id=id)

    context = {
        'article':article,
    }

    return render(request, 'detail.html', context)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article) # 새로운 정보, instance = 기존 정보
            if form.is_valid():
                form.save()
                return redirect('articles:detail', id=id)

    else:
        form = ArticleForm(instance=article) #instance

    context = {
        'form':form,
    }

    return render(request, 'update.html', context)

def delete(reqeust, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')