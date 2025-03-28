## 1-N
- 하나의 상위 개념에 속해있을 때
- 정규화 : 데이터 베이스는 셀 하나에 하나의 데이터를 지향함.   
    - 정규 이상 
    - 삭제 이상
- 테이블 2개 만들기 / post_id의 중복 제거 (게시글의 내용이 같더라도 고유의 아이디 지님.)
    - 테이블 1 : id(post) / title, comment
    - 테이블 2 : id (primary key) / post_id / comments

- ex : github

## 0. django 설정
`pip install django`
- 프로젝트 생성 django-admin startproject crud . (. 현재 파일에 생성)
- 앱 생성 django-admin startapp posts (posts라는 앱 생성)
- 앱 등록 (setting)
    posts (앱 이름 적어주기) 

- 밖에 temlates 폴더 생성 
    `'DIRS': [BASE_DIR / 'templates'],`
- teplates에 `base.html`
```shell
<body> 
    {% block body %} # 기본 틀 만들고 난 이후
    {% endblock %}
</body>
```
## modeling
- 1) 게시글 (첫번째 테이블)
```python
class Article(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) 
    # 수정되는 시간을 자동 저장
    updated_at = models.DateTimeField(auto_now = True) 
    # 현재 시간을 자동 저장
```

- 2) 댓글 기능 구현 (두번째 테이블)
```python
class comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # 외래 키 : 부모의 아이디값이 저장되는 공간 / 
    # on_delete : 부모가 지워졌을때 / CASCADE :부모, 자식 모두 지워주는
```
## migraions
- 모델링 한 이후에는 반드시 마이그레이션 해야 함.
`python manage.py makemigrations`
`python manage.py migrate`

## Create 구현
- `articles앱 내에 (forms.py)`
```python
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__' # 모든 필드를 불러옴.
```

- `(urls.py)`
```python
# create
    path('create/', views.create, name = 'create'), 
    # new와 create 한번에 처리
```

- `views.py`
```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else:     # 1. GET 요청 : 비어있는 form (new) 먼저 만들기 
        form = ArticleForm()

    context = {
        'form':form,
    }

    return render(request, 'create.html', context)
```

- `create.html` 
```python
{% extends 'base.html' %}

{% block body %}
<form action="" method="POST">
    {% csrf_token %} # 메소드가 post면 csrf token을 넣어야 함.
    {{form}}
    <input type="submit">
</form>
{% endblock %}
```

## Read 구현



## update 구현
- `urls.py`
```python
path('<int:id>/update/', views.update, name= 'update'),
```

- `views.py`
```python 
def update(request, id):
    # if와 else가 중복되므로 업데이트할 아이디 찾기
    article = Article.objects.get(id=id) 
    
    if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article) 
            # request.POST = 새로운 정보, instance = 기존 정보
            if form.is_valid(): # form에 대해 유효성 검사
                form.save()
                return redirect('articles:index')

    else:
        form = ArticleForm(instance=article) #instance

    context = {
        'form':form,
    }

    return render(request, 'update.html', context)
```

## comment create


`IntegrityError at /articles/7/comments/create/`
    - `NOT NULL constraint failed:` : article_id를 빠뜨림.


## 
`views.py - def detail`
```python
comments = article.comment_set.all() # 해당하는 게시글에 속하는 댓글만 불러옴.

'comments':comments,
```
`detail.html`
```python
{% extends 'base.html' %}

{% block body %}

    <h3>{{article.title}}</h3>
    <p>{{article.content}}</p>
    <p>{{article.created_at}}</p>
    <p>{{article.updated_at}}</p>
    
    <a href="{% url 'articles:update' article.id %}">update</a>
    <a href="{% url 'articles:delete' article.id %}">delete</a>

    <hr>

    <form action="{% url 'articles:comment_create' article.id %}" method="POST">
        {% csrf_token %}
        {{form}}
        <input type="submit">
    </form>

    <hr> 

    {% for comment in comments %} 
        <li>{{comment.content}}</li>
    # article이 가지고 있는 자식 article을 모두 가져옴.
    
    {% endfor %}

{% endblock %}
```
### comment update
- 댓글 수정 (개발자 모드)
`li 태그를 input으로 변경`


## comment delete
- `urls.py`
```python
 # Delete
    path('<int:article_id>/comments/<int:id>/delete', views.comment_delete, name = 'comment_delete'),
    #article/2/comments/2/delete
```

- `views.py`
```python
def comment_delete(request, article_id, id): # id의 id값을 찾음.
    comment = Comment.objects.get(id=id)
    comment.delete()

    return redirect('articles:detail', id=article_id) # detail로 돌아감.
```

- `detail.html`
```python
<hr> 

    {% for comment in comments %}
        <li>{{comment.content}}</li>
        <a href="{% url 'articles:comment_delete' article.id comment.id %}">delete</a>
    {% endfor %}

{% endblock %}
```