from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_dec = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA7GbKZJfH2z_BfU46jgCuiv2y73UaR0gpQg&usqp=CAU')
