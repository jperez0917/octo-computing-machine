from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from links.models import Link


class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'


class LinkDetailView(DetailView):
    model = Link
    template_name = 'links\link_detail.html'


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'links\link_create.html'
    fields = ('url', 'url_label', 'notes', 'public')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LinkEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Link
    template_name = 'links\link_edit.html'
    fields = ('url', 'url_label', 'notes', 'public')

    def test_func(self):
        link = self.get_object()
        return self.request.user == link.owner