from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # create
    path('create/', views.create, name = 'create'),
    # Read

    # Update

    # Delete
]