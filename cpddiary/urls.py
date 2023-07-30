from django.urls import path
from .views import DiaryList, DiaryDetail

urlpatterns = [
    path('', DiaryList.as_view(), name="cpdlist"),
    path('diary_entry/<int:pk>/', DiaryDetail.as_view(), name='cpdlist'),
]