from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def indexPageView(request):
    sOutput = 'Index (landing) Page'
    return HttpResponse(sOutput)


def AddTShirtPageView(request):
    sOutput = 'Add T Shirt Attributes Page'
    return HttpResponse(sOutput)


def RankingPageView(request):
    sOutput = 'Ranking Page'
    return HttpResponse(sOutput)