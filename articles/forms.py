from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields => 추가할 필드 목록
        # fields = ('content', ) # article을 연결하는 부분을 content만으로 바꿈.
        
        # exclude => 제외할 필드 목록
        exclude = ('article', )