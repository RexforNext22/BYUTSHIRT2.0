from django.contrib import admin

# Register your models here.
from .models import Material, Category, Size, PrimaryColor, ArticleOfClothing

admin.site.register(Material)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(PrimaryColor)
admin.site.register(ArticleOfClothing)