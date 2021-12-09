from django.urls import path
from .views import indexPageView, AddTShirtPageView, DeleteTShirtPageView, AboutTShirtPageView, RankingPageView, EditPageView
from .views import showSingleArticlePageView, SaveTShirtPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Add/", AddTShirtPageView, name="add"),
    path("Delete/", DeleteTShirtPageView, name="delete"),
    path("about/", AboutTShirtPageView, name="about"),
    path("Rank/", RankingPageView, name="ranking"),
    path("Edit/", EditPageView, name="edit"),
    path("showSingleArticle/<int:item_id>/", showSingleArticlePageView,
         name="showSingleArticle"),  # Show an individual
    path("save/", SaveTShirtPageView, name="save")
]
