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

    context = {
        "lstMaterials" : lstMaterials,
        "lstSize" : lstSize,
        "lstCategory" : lstCategory
    }


    return render(request, 'RanktShirts/add.html', context)


def SaveTShirtPageView(request):
    if request.method == 'POST' :
        oArticleOfClothing = ArticleOfClothing()


        oArticleOfClothing.clothing_name = request.POST.get('clothing_name')
        oArticleOfClothing.price = request.POST['price']
        oArticleOfClothing.material_name = request.POST['material']


        oArticleOfClothing.category_name = request.POST['category']
        oArticleOfClothing.size_name = request.POST['size']
        oArticleOfClothing.color_name = request.POST['pColor']

        # print(oArticleOfClothing)
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


def EditPageView(request, AoC_id):
    data = ArticleOfClothing.objects.get(id = AoC_id)
    context = {
        "ArticleOfClothing": data,
    }

    return render(request, 'RanktShirts/edit.html', context)


def showSingleArticlePageView(request, item_id):
    data = ArticleOfClothing.objects.get(id=item_id)
    context = {
        "ArticleOfClothing": data,
    }

    return render(request, 'RanktShirts/showItem.html', context)
    

   

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


