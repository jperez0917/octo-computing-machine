from django.views.generic import ListView

from links.models import Link

class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'
