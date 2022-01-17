from django.shortcuts import render
from .models import Articles, Articles_principale, Articles_secondaire, Derniers_Articles
from django.shortcuts import get_object_or_404



# Create your views here.
def articles_view(request):
    articles=Articles.objects.all()
    articlesp=Articles_principale.objects.all()
    articless=Articles_secondaire.objects.all()
    darticles=Derniers_Articles.objects.all()
    return render(request,'art24/articles.html', context={'articles': articles ,'articlesp':articlesp ,'articless':articless,'darticles':darticles})



def article_view(request, article): 
    article=Articles.objects.get(slug=article)
    return render(request,'art24/detail.html', context={'article': article })


def articlep_view(request, articlep): 
    articlep=Articles_principale.objects.get(slug=articlep)
    return render(request,'art24/detail.html', context={'articlep': articlep})
