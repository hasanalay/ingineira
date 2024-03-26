from django.contrib import admin
from .models import Service, Article

class ServiceAdmin(admin.ModelAdmin):
    verbose_name = 'Service Item'
    verbose_name_plural = 'Service Items'


class ArticleAdmin(admin.ModelAdmin):
    verbose_name = 'Article Item'
    verbose_name_plural = 'Article Items'


admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)
