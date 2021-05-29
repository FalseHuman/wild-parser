from django.db import models

class Product(models.Model):
   product = models.CharField('Название товара', max_length=200)