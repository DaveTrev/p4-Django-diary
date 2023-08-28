from django.urls import path
from .views import (
    DiaryListView,
    DiaryDetailView,
    DiaryCreateView,
    DiaryUpdateView,
    DiaryDeleteView,
    CpdLoginView,)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CpdLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('', DiaryListView.as_view(), name="entry-list"),
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