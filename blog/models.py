from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254)
    summary = models.TextField(max_length=150)
    content = models.TextField(max_length=4000, blank=True)
    date = models.DateField(auto_now_add=True)
    date = models.TimeField(auto_now_add=True)
    tag = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    photo = models.ImageField(max_length=200)

    def __str__(self):
        return self.title
