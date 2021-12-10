from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# Import models
from .models import Material
from .models import Category
from .models import Size
from .models import ArticleOfClothing, PrimaryColor


def indexPageView(request):

    return render(request, 'RanktShirts/index.html')


def AddTShirtPageView(request):

    lstMaterials = ["Cotton", "Wool", "Plastic"]
    lstSize = ["XXL", "XL", "L", "M", "S", "XS", "XXS"]
    lstCategory = ["Shirt", "Sweater", "Hoodie"]
    lstColor = ["Blue", "Red", "White", "Yellow", "Green", "Purple", "Orange"]

    context = {
        "lstMaterials": lstMaterials,
        "lstSize": lstSize,
        "lstCategory": lstCategory,
        "lstColor": lstColor
    }

    return render(request, 'RanktShirts/add.html', context)


def SaveTShirtPageView(request):
    if request.method == 'POST':
        oArticleOfClothing = ArticleOfClothing()

        oArticleOfClothing.clothing_name = request.POST.get('clothing_name')
        oArticleOfClothing.price = request.POST['price']
        oArticleOfClothing.material_id = request.POST['material']

        oArticleOfClothing.category_id = request.POST['category']
        oArticleOfClothing.size_id = request.POST['size']
        oArticleOfClothing.primarycolor_id = request.POST['pColor']

        # print(oArticleOfClothing)
        oArticleOfClothing.save()

    return render(request, 'RanktShirts/ranking.html')


def DeleteTShirtPageView(request, ArticleOfClothingID):
    data = ArticleOfClothing.objects.get(id=ArticleOfClothingID)
    data.delete()
    return indexPageView(request)


def AboutTShirtPageView(request):
    return render(request, 'RanktShirts/about.html')


def RankingPageView(request):
    data = ArticleOfClothing.objects.all()
    context = {
        "ArticleOfClothing": data,
    }
    return render(request, 'RanktShirts/ranking.html', context)


def EditPageView(request, AoC_id):
    data = ArticleOfClothing.objects.get(id=AoC_id)
    lstMaterials = ["Cotton", "Wool", "Plastic"]
    lstSize = ["XXL", "XL", "L", "M", "S", "XS", "XXS"]
    lstCategory = ["Shirt", "Sweater", "Hoodie"]

    context = {
        "ArticleOfClothing": data,
        "lstMaterials": lstMaterials,
        "lstSize": lstSize,
        "lstCategory": lstCategory
    }

    return render(request, 'RanktShirts/edit.html', context)


def showSingleArticlePageView(request, item_id):
    data = ArticleOfClothing.objects.get(id=item_id)
    context = {
        "ArticleOfClothing": data,
    }

    return render(request, 'RanktShirts/showItem.html', context)


def UpdateArticlePageView(request, AoC_id):
    if request.method == 'POST':
        article = ArticleOfClothing.objects.get(id=AoC_id)

        article.clothing_name = request.POST['clothing_name']
        article.price = request.POST['price']
        article.material_name = request.POST['material_name']
        article.category_name = request.POST['category_name']
        article.size_name = request.POST['size_name']
        article.color_name = request.POST['color_name']

        article.save()

    return RankingPageView(request)
