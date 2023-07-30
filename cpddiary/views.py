from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import diary_entry
# Create your views here.


class DiaryList(ListView):
    model = diary_entry
    context_object_name = 'entry'


class DiaryDetail(DetailView):
    model = diary_entry
    context_object_name = 'entry'
    
