from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Material(models.Model):
    material_name = models.CharField(max_length=20, unqiue=True)
            
    def __str__(self) :
        return (self.description)

class Category(models.Model):
    category_name = models.CharField(max_length=20, unqiue=True)
            
    def __str__(self) :
        return (self.description)

class Size(models.Model):
    size_name = models.CharField(max_length=3, unqiue=True)
            
    def __str__(self) :
        return (self.description)

class PrimaryColor(models.Model):
    color_name = models.CharField(max_length=20, unqiue=True)
            
    def __str__(self) :
        return (self.description)

class ArticleofClothing(models.Model):
    clothing_name = models.CharField(max_length=20)
    rank = models.IntegerField(default = 0)
    price = models.DecimalField((""), max_digits=5, decimal_places=2)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING, to_field='material_name')
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, to_field='size_name')
    primarycolor = models.ForeignKey(PrimaryColor, on_delete=models.DO_NOTHING, to_field='color_name')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, to_field='category_name')
    photo_main = models.ImageField(upload_to='photos')
            
    def __str__(self) :
        return (self.description)

    def save(self):
        self.clothing_name = self.clothing_name.capitalize()
        super(ArticleofClothing, self).save()