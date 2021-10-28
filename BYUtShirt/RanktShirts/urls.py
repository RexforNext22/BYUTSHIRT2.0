from django.urls import path
from .views import indexPageView, AddTShirtPageView, DeleteTShirtPageView, EditTShirtPageView, RankingPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Add/", AddTShirtPageView, name="AddTShirt"),
    path("Delete/", DeleteTShirtPageView, name="DeleteTShirt"),
    path("Edit/", EditTShirtPageView, name="EditTShirtPageView"),
    path("Rank/", RankingPageView, name="RankingPageView"),
]
