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


def DeleteTShirtPageView(request):
    return render(request, 'RanktShirts/delete.html')


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
