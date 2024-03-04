from django.contrib import admin
from .models import About, News, Service, Team, Contact, Article
class AboutAdmin(admin.ModelAdmin):
    verbose_name = 'About Item'
    verbose_name_plural = 'About Items'

class NewsAdmin(admin.ModelAdmin):
    verbose_name = 'News Item'
    verbose_name_plural = 'News Items'

class ServiceAdmin(admin.ModelAdmin):
    verbose_name = 'Service Item'
    verbose_name_plural = 'Service Items'

class TeamAdmin(admin.ModelAdmin):
    verbose_name = 'Team Item'
    verbose_name_plural = 'Team Items'

class ContactAdmin(admin.ModelAdmin):
    verbose_name = 'Contact Item'
    verbose_name_plural = 'Contact Items'
    
class ArticleAdmin(admin.ModelAdmin):
    verbose_name = 'Article Item'
    verbose_name_plural = 'Article Items'

admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Article, ArticleAdmin)
