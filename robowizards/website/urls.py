from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('news/', views.news, name='news'),
    # path('services/', views.services, name='services'),
    # path('team/', views.team, name='team'),
    # path('contact/', views.contact, name='contact'),
    # path('index/', views.index, name='index'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
