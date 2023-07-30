from django.urls import path
from .views import DiaryList, DiaryDetail

urlpatterns = [
    path('', DiaryList.as_view(), name="cpdlist"),
    path('entry/<int:pk>/', DiaryDetail.as_view(), name='cpdlist'),
]