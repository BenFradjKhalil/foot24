from django.shortcuts import render
from .models import Articles, Articles_principale, Articles_secondaire
from django.http.response import HttpResponse

# Create your views here.
def articles_view(request):
    articles=Articles.objects.all()
    articlesp=Articles_principale.objects.all()
    articless=Articles_secondaire.objects.all()
    return render(request,'art24/articles.html', context={'articles': articles ,'articlesp':articlesp ,'articless':articless})





def article_view(request, slug): 
    return HttpResponse("Page d'article")