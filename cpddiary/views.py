from django.shortcuts import render
from django.views.generic.list import ListView
from .models import diary_entry
# Create your views here.


class DiaryList(ListView):
    model = diary_entry
