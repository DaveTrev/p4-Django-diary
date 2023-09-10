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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.template import RequestContext
from .models import Entry
from .forms import EntryForm


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = 'about.html'


class DiaryListView(LoginRequiredMixin, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date")
    context_object_name = 'entries'
    template_name = 'entry_list.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        search_bar = self.request.GET.get('search-page') or ''
        if search_bar:
            queryset = queryset.filter(title__icontains=search_bar)
        return queryset.order_by("-date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_bar = self.request.GET.get('search-page') or ''
        context['search_bar'] = search_bar
        return context


# possible change to search bar needed, how to refresh in real time
# https://stackoverflow.com/questions/61446467/how-to-make-a-search-bar-that-refresh-everytime-the-user-input-something


class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class DiaryCreateView(LoginRequiredMixin, UserPassesTestMixin,
                      SuccessMessageMixin, CreateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("entry-list")
    success_message = "Your new CPD diary entry was created!"
    # Success message may need JS script to set time

    def test_func(self):
        return self.request.user.is_authenticated
      
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


class DiaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your diary entry was deleted!"

    def test_func(self):
        entry = self.get_object()
        return entry.user == self.request.user

    def delete(self, request, *args, **kwargs):
        if self.test_func():
            messages.success(self.request, self.success_message)
            return super().delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()


def Custom_404(request, exception):
    return render(request, '404.html', {})


def Custom_500(request):
    return render(request, '500.html', {})