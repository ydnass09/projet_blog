from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article.titre}"

