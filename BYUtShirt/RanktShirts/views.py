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


def DeleteTShirtPageView(request, ArticleOfClothingID):
    data = ArticleOfClothing.objects.get(id=ArticleOfClothingID)
    data.delete()
    return RankingPageView(request)


def AboutTShirtPageView(request):
    return render(request, 'RanktShirts/about.html')


def RankingPageView(request):
    data = ArticleOfClothing.objects.all()
    context = {
        "ArticleOfClothing" : data,
    }
    return render(request, 'RanktShirts/ranking.html', context)
    

def EditPageView(request):
    return render(request, 'RanktShirts/edit.html')

def showSingleArticlePageView(request, item_id):
    data = ArticleOfClothing.objects.get(id = item_id)
    context = {
        "ArticleOfClothing" : data,
    }

    return render(request, 'RanktShirts/showItem.html', context)

