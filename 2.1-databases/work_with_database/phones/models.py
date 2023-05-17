from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.ImageField()
    release_date = models.DateField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, null=False)
