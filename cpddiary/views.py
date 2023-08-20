from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Entry


class DiaryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date")


class DiaryDetailView(DetailView):
    model = Entry
