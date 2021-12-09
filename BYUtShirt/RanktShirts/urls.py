from django.urls import path
from .views import indexPageView, AddTShirtPageView, DeleteTShirtPageView, AboutTShirtPageView, RankingPageView, EditPageView
from .views import showSingleArticlePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Add/", AddTShirtPageView, name="add"), # Navigate to the add page
    path("Delete/", DeleteTShirtPageView, name="delete"), #delete
    path("about/", AboutTShirtPageView, name="about"), # Navigate to the about page
    path("Rank/", RankingPageView, name="ranking"), # Navigate to the ranking page
    path("Edit/", EditPageView, name="edit"), # Navigate to the edit page
    path("showSingleArticle/<int:item_id>/", showSingleArticlePageView, name="showSingleArticle") # Show an individual article of clothing
]

