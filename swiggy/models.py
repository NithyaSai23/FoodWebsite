from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Item(models.Model):
#1. Restarantname 2. Food name 3. Place  4. cost 5. Rating  6. Add item image
    foodid=models.IntegerField()
    restaurantname=models.CharField(max_length=50)
    foodname=models.CharField(max_length=50)
    cost=models.FloatField()
    rating=models.FloatField()
    food_image=models.ImageField(upload_to='images/',default="")

