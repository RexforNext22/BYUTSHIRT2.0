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

    return render(request, 'RanktShirts/add.html')


def SaveTShirtPageView(request):
    oArticleOfClothing = ArticleOfClothing()

    oArticleOfClothing.clothing_name = request.POST['clothing_name']
    oArticleOfClothing.price = request.POST['price']
    oArticleOfClothing.material = request.POST['material']
    oArticleOfClothing.category = request.POST['category']
    oArticleOfClothing.size = request.POST['size']
    oArticleOfClothing.primarycolor = request.POST['pColor']

    oArticleOfClothing.save()
    return render(request, 'RanktShirts/index.html')


def DeleteTShirtPageView(request):
    return render(request, 'RanktShirts/delete.html')


def AboutTShirtPageView(request):
    return render(request, 'RanktShirts/about.html')


def RankingPageView(request):
    data = ArticleOfClothing.objects.all()
    context = {
        "ArticleOfClothing": data,
    }
    return render(request, 'RanktShirts/ranking.html', context)


def EditPageView(request):
    return render(request, 'RanktShirts/edit.html')


def showSingleArticlePageView(request, item_id):
    data = ArticleOfClothing.objects.get(id=item_id)
    context = {
        "ArticleOfClothing": data,
    }

    return render(request, 'RanktShirts/showItem.html', context)
