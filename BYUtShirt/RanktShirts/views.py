from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def indexPageView(request):
    
    return render(request, 'RanktShirts/index.html')


def AddTShirtPageView(request):
  return render(request, 'RanktShirts/add.html')


def DeleteTShirtPageView(request):
    return render(request, 'RanktShirts/delete.html')


def AboutTShirtPageView(request):
    return render(request, 'RanktShirts/about.html')


def RankingPageView(request):
    return render(request, 'RanktShirts/ranking.html')

def EditPageView(request):
    return render(request, 'RanktShirts/edit.html')
