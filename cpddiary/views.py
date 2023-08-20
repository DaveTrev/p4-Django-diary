from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Entry
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class DiaryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date")


class DiaryDetailView(DetailView):
    model = Entry


class DiaryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new CPD diary entry was created!"


class DiaryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]
    success_message = "Your new CPD diary entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )


class DiaryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your diary entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(reqeust, *args, **kwargs)
