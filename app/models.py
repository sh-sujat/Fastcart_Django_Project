from django.db import models


class ProfilePic(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='ProfilePic')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=20)
    discount = models.FloatField(max_length=20, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Products')

    def __str__(self):
        return self.name
