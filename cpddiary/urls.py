from django.urls import path
from .views import (
    DiaryListView,
    DiaryDetailView,
    DiaryCreateView,
    DiaryUpdateView,
    DiaryDeleteView,
    AboutPageView,
    HomePageView,
    )
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('entrylist/', DiaryListView.as_view(), name="entry-list"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('entry/<int:pk>/',
         DiaryDetailView.as_view(),
         name='entry-detail'),
    path("create/",
         DiaryCreateView.as_view(),
         name='entry-create'),
    path("entry/<int:pk>/update",
         DiaryUpdateView.as_view(),
         name='entry-update'),
    path("entry/<int:pk>/delete",
         DiaryDeleteView.as_view(),
         name='entry-delete'),
]