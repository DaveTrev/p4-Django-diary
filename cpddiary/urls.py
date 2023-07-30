from django.urls import path
from .views import DiaryList

urlpatterns = [
    path('', DiaryList.as_view(), name="diary-entry"),
]