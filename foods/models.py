from django.db import models

# Create your models here.
class Food(models.Model):
    FOOD_TYPE = [
        ("lunch", "Lunch"),
        ("dinner", "Dinner")
    ]
    name = models.CharField(max_length=100, default=None)
    description = models.TextField(max_length=500, default=None)
    rate = models.IntegerField(default=0)
    price = models.IntegerField(default=None)
    time = models.IntegerField(default=None)
    tags = models.CharField(max_length=50, default=None)
    food_type = models.CharField(max_length=10, choices=FOOD_TYPE, default="dinner")
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='foods/', default=None)

    def __str__(self):
        return self.name
