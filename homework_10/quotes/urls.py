from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<str:_id>', views.author_info, name='author_info'),
    path('add_quote', views.add_quote, name='add_quote'),
    path('add_author', views.add_author, name='add_author'),
]