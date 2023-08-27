from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry


class CpdLoginView(LoginView):
    template_name = 'cpddiary/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("entry-list")


class DiaryListView(LoginRequiredMixin, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date")
    template_name = 'entry_list.html'
    

class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class DiaryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new CPD diary entry was created!"


class DiaryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]
    success_message = "Your new CPD diary entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-list",
        )


class DiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your diary entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
