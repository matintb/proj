from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

    
class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class post(models.Model):   
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)                
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True) 
    updated_date = models.DateTimeField(auto_now=True)
    
    # meta dar hamon admin zaher mishe
    class Meta:
        ordering = ['created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        
    
    def __str__(self):
        return " {} - {} ".format(self.title,self.id)
    
    def snippets(self):
        return self.content[:100]+'...'
    
        # for /sitemap.xml + add a button in admin/post
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    
class comments(models.Model):
    Post = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_date']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name