from django.shortcuts import render, get_object_or_404
from .models import Article, Categorie, Commentaire

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    commentaires = Commentaire.objects.filter(article=article)
    return render(request, 'blog/detail_article.html', {'article': article, 'commentaires': commentaires})

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'blog/liste_categories.html', {'categories': categories})

def articles_par_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    articles = Article.objects.filter(categorie=categorie)
    return render(request, 'blog/articles_par_categorie.html', {'categorie': categorie, 'articles': articles})

