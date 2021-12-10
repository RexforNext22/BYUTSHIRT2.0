from django.urls import path
from .views import SaveTShirtPageView, indexPageView, AddTShirtPageView, DeleteTShirtPageView, AboutTShirtPageView, RankingPageView, EditPageView
from .views import showSingleArticlePageView, UpdateArticlePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Add/", AddTShirtPageView, name="add"),
    path("Delete/<int:ArticleOfClothingID>", DeleteTShirtPageView, name="delete"),
    path("about/", AboutTShirtPageView, name="about"),
    path("Rank/", RankingPageView, name="ranking"),
    path("Edit/<int:AoC_id>", EditPageView, name="edit"),
    path("showSingleArticle/<int:item_id>/", showSingleArticlePageView, name="showSingleArticle"),  # Show an individual
    path("updateArticle/<int:AoC_id>", UpdateArticlePageView, name="update"),
    path("Save/", SaveTShirtPageView, name="save")
]
