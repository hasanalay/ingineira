from django.db import models
# I am going to change all models for my new index page later.

class About(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)
    Created = models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to='about_image/', null=True, blank=True) 
    
    def __str__(self):
        return self.Title
    
class News(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)
    Created = models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to='new_image/', null=True, blank=True) 
    
    def __str__(self):
        return self.Title
    
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)
    Linkedin = models.URLField(max_length=200, null=True, blank=True)
    Created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name
    
class Team(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField(max_length=200)
    Created = models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to='team_member_image/', null=True, blank=True)
    
    def __str__(self):
        return self.Name

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
