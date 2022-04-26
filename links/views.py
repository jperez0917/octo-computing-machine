from django.views.generic import ListView, CreateView, DetailView

from links.models import Link


class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'


class LinkCreateView(CreateView):
    model = Link
    template_name = 'links\link_create.html'
    fields = ('url', 'url_label', 'notes', 'public', 'owner')


class LinkDetailView(DetailView):
    model = Link
    template_name = 'links\link_detail.html'

