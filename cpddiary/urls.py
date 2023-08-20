from django.urls import path
from .views import DiaryListView, DiaryDetailView

urlpatterns = [
    path('', DiaryListView.as_view(), name="diary-list"),
    path('entry/<int:pk>/', DiaryDetailView.as_view(),
         name='diary-detail'),
]