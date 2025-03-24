from django.shortcuts import render, redirect
from .forms import ArticleForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles.index')
    
    else:            # new 먼저 
        form = ArticleForm()

    context = {
        'form':form,
    }

    return render(request, 'create.html', context)