from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from links.models import Link


class LinkListView(ListView):
    model = Link
    template_name = 'links/link_home.html'


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


class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Link
    template_name = 'links\link_delete.html'
    success_url = reverse_lazy('links:list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.owner
