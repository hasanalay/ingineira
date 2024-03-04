from django.shortcuts import render, HttpResponse
from . models import About, News, Service, Team , Contact, Article

def index(request):
    latest_articles = Article.objects.order_by('-Created')[:4]
    latest_services = Service.objects.order_by('-Created')[:6]
    return render(request, 'index.html', {
        'articles': latest_articles,
        'services': latest_services
        
    })

# def article (request):
#     articles = Article.objects.all()
#     return render(request, 'index.html', {
#         'articles': articles
#     })

# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     abouts = About.objects.all()
#     return render(request, 'about.html', {
#         'abouts': abouts
#     })
    
# def news(request):
#     news = News.objects.all()
#     return render(request, 'news.html', {
#         'news': news
#     })
    
# def services(request):
#     services = Service.objects.all()
#     return render(request, 'services.html', {
#         'services': services
#     })

# def team(request):
#     teams = Team.objects.all()
#     return render(request, 'team.html', {
#         'teams': teams
#     })
    
# def contact(request):
#     contacts = Contact.objects.all()
#     return render(request, 'contact.html', {
#         'contacts': contacts
#     })
    