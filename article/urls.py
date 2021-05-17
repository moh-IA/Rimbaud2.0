from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('article/<article_id>/', views.article, name= 'article'),
    path('search_articles', views.search_article, name= 'search-articles'),
]