from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from links.models import Link


class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'links\link_create.html'
    fields = ('url', 'url_label', 'notes', 'public')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LinkDetailView(DetailView):
    model = Link
    template_name = 'links\link_detail.html'

