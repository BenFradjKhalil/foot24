from django.shortcuts import render
from art24.models import Articles
from django.http.response import HttpResponse



def home_view(request):
    return render(request,'index.html')

def articles_view(request):
    articles=Articles.objects.all()
    return render(request,'foot24/index.html', context={'articles': articles})


def article_view(request, slug): 
    return HttpResponse("Page d'article")