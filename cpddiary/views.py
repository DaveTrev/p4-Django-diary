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


class DiaryListView(LoginRequiredMixin, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date")
    context_object_name = 'entries'
    template_name = 'entry_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = context['entries'].filter(user=self.request.user)

        search_bar = self.request.GET.get('search-page') or ''
        if search_bar:
            context['entries'] = context['entries'].filter(
                title__icontains=search_bar)
                #possible change to search bar needed, how to refresh in real time
        #https://stackoverflow.com/questions/61446467/how-to-make-a-search-bar-that-refresh-everytime-the-user-input-something

        context['search_bar'] = search_bar
        return context


class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class DiaryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "learningOutcome", "activityType", "timeSpent",
              "cpdCredits", "practiceImpact"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new CPD diary entry was created!"
    # Success message may need JS script to set time

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DiaryCreateView, self).form_valid(form)


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
