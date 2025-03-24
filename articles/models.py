from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # comment_set = 
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # 외래 키 : 부모의 아이디값이 저장되는 공간 / 
    # on_delete : 부모가 지워졌을때 / CASCADE :부모, 자식 모두 지워주는

    # article_id = 