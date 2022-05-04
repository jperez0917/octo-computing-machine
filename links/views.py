from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from links.models import Link
from accounts.models import CustomUser


class PublicLinkListView(ListView):
    # model attribute not needed since we are using get_queryset.
    # model = Link
    template_name = 'links/links_public.html'

    def get_queryset(self):
        return Link.objects.filter(public=True)


class LinkListView(LoginRequiredMixin, ListView):
    template_name = 'links/links_list.html'

    def get_queryset(self):
        print(self.request.user.id)
        return Link.objects.filter(owner=self.request.user.id)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


class LinkUserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'links/link_user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return_object =  get_object_or_404(CustomUser, username=self.request.user)
        return return_object
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are adding more 'context' attributes.
        # print(context)
        # print(context.keys())
        context['number_of_links'] = Link.objects.filter(owner=self.request.user.id).count()
        # context[] = <another item>
        return context    


class LinkDetailView(LoginRequiredMixin, DetailView):
    model = Link
    template_name = 'links/link_detail.html'


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'links/link_create.html'
    fields = ('url', 'url_label', 'notes', 'public')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LinkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Link
    template_name = 'links/link_edit.html'
    fields = ('url', 'url_label', 'notes', 'public')

    def test_func(self):
        link = self.get_object()
        return self.request.user == link.owner


class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Link
    template_name = 'links/link_delete.html'
    success_url = reverse_lazy('links:profile')

    def test_func(self):
        link = self.get_object()
        return self.request.user == link.owner
