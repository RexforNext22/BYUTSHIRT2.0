from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class Material(models.Model):
    material_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return (self.material_name)


class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return (self.category_name)


class Size(models.Model):
    size_name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return (self.size_name)


class PrimaryColor(models.Model):
    color_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return (self.color_name)


class ArticleOfClothing(models.Model):
    clothing_name = models.CharField(max_length=20)
    price = models.DecimalField((""), max_digits=5, decimal_places=2)
    material = models.ForeignKey(
        Material, on_delete=models.DO_NOTHING, to_field='material_name')
    size = models.ForeignKey(
        Size, on_delete=models.DO_NOTHING, to_field='size_name')
    primarycolor = models.ForeignKey(
        PrimaryColor, on_delete=models.DO_NOTHING, to_field='color_name', verbose_name="Primary Color")
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, to_field='category_name')

    def __str__(self):
        return (self.clothing_name)

    # def save(self):
    #     # self.clothing_name = self.clothing_name.capitalize()
    #     super(ArticleOfClothing, self).save()
