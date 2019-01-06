from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, default='Item.')
    description = models.CharField(max_length=500, default='An item.')
    price = models.IntegerField(default=0)

    brand = models.ForeignKey('essence_web_app.Brand', related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey('essence_web_app.Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('essence_web_app.SubCategory', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)

    category = models.ForeignKey('essence_web_app.Category', related_name='subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Picture(models.Model):
    pic_name = models.CharField(max_length=150)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.pic_name
