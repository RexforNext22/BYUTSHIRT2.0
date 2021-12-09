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
    

def EditPageView(request, AoC_id):
    data = ArticleOfClothing.objects.get(id = AoC_id)

    context = {
        "ArticleOfClothing" : data,
    }

    return render(request, 'RanktShirts/edit.html', context)

def updatePrescriberPageView(request, AoC_id) :
    if request.method == 'POST' :
        prescriber_id = request.POST['NPI']
        article = ArticleOfClothing.objects.get(id = AoC_id)

        article.clothing_name = request.POST['NPI']
        article.fname = request.POST['first_name']
        article.lname = request.POST['last_name']
        article.gender = request.POST['gender']
        article.state_id = request.POST['state']
        article.credentials = request.POST['credentials']

        
        
        article.save()
     

    return savePageView(request)

