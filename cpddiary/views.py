from django.shortcuts import render
from django.urls import reverse_lazy
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


class DiaryCreateView(CreateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]
    success_url = reverse_lazy("entry-list")


class DiaryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )


class DiaryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
