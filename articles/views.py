from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
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

def detail(request,id): # 게시글 보여주기
    article = Article.objects.get(id=id)
    comments = article.comment_set.all() # 해당하는 게시글에 속하는 댓글만 불러옴.
    form = CommentForm()

    context = {
        'article':article,
        'form':form,
        'comments':comments,
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


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)   # 댓글 완전히 저장 x , 줘야 할 정보가 남아있음.
            
            article = Article.objects.get(id=article_id) # 내가 속한 부모가 되는 정보를 찾음.
            comment.article = article
            comment.save()

            return redirect('articles:detail', id=article_id)
    else:
        return redirect('articles:index')