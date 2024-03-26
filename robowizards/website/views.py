from django.shortcuts import render, HttpResponse
from . models import  Service, Article

def index(request):
    latest_articles = Article.objects.order_by('-Created')[:4]
    latest_services = Service.objects.order_by('-Created')[:6]
    return render(request, 'index.html', {
        'articles': latest_articles,
        'services': latest_services
        
    })