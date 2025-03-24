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
]