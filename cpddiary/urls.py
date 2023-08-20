from django.urls import path
from .views import (
    DiaryListView,
    DiaryDetailView,
    DiaryCreateView,
    DiaryUpdateView,
    DiaryDeleteView)

urlpatterns = [
    path('', DiaryListView.as_view(), name="diary-list"),
    path('entry/<int:pk>/',
         DiaryDetailView.as_view(),
         name='diary-detail'),
    path("create",
         DiaryCreateView.as_view(),
         name='diary-create'),
    path("entry/<int:pk>/update",
         DiaryUpdateView.as_view(),
         name='diary-update'),
    path("entry/<int:pk>/delete",
         DiaryDeleteView.as_view(),
         name='diary-delete'),
]