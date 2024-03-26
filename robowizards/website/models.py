from django.db import models

class Service(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=1000)
    Created = models.DateTimeField(auto_now_add=True)
    Image1 = models.ImageField(upload_to='service_image/', null=True, blank=True)
    Image2 = models.ImageField(upload_to='service_image/', null=True, blank=True)
    Image3 = models.ImageField(upload_to='service_image/', null=True, blank=True)
    Image4 = models.ImageField(upload_to='service_image/', null=True, blank=True)
    
    def __str__(self):
        return f'Title: {self.Title}  |  Date: {self.Created.strftime("%Y-%m-%d %H:%M:%S")}'


class Article (models.Model):
    Title = models.CharField(max_length=200)
    Category = models.CharField(max_length=50)
    Created = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(upload_to='article_image/')
    URL = models.URLField(max_length=200)
    
    def __str__(self):
        return f'Title: {self.Title}  |  Date: {self.Created.strftime("%Y-%m-%d %H:%M:%S")}'
