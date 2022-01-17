from django.db import models

# Create your models here.
class Articles(models.Model):
    contenu=models.TextField()
    slug=models.SlugField(max_length=150)
    date_publication=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(default='default.jpg')
    
    def __str__(self):
        return self.contenu

class Articles_principale(models.Model):
    contenu=models.TextField() 
    slug=models.SlugField(max_length=150)
    date_publication=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(default='default.jpg')
    
    def __str__(self):
        return self.contenu
    
class Articles_secondaire(models.Model):
    contenu=models.TextField()
    slug=models.SlugField(max_length=150)
    date_publication=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(default='default.jpg')
    
    def __str__(self):
        return self.contenu
    
    
