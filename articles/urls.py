from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # create
    path('create/', views.create, name = 'create'), # new와 create 한번에 처리

    # Read
    path('', views.index, name= 'index'),
    path('<int:id>/', views.detail, name= 'detail'),

    # Update
    path('<int:id>/update/', views.update, name= 'update'),

    # Delete
    path('<int:id>/delete/', views.delete, name = 'delete'),

    # Commnet
    # Create
    path('<int:article_id>/comments/create/', views.comment_create, name = 'comment_create'),

    # Delete
    path('<int:article_id>/comments/<int:id>/delete', views.comment_delete, name = 'comment_delete'),
    #article/2/comments/2/delete
]