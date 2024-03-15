from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categorie/<int:categorie_id>/', views.articles_par_categorie, name='articles_par_categorie'),
]

