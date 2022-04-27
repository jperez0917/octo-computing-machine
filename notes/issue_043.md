## Issue 43 - Links have a delete view
[Issue 43](https://github.com/jperez0917/octo-computing-machine/issues/43)

### Resources:

* https://github.com/django/django

### Commands, virtual environment, etc:

* Virtual environment activation:
    * Powershell: `C:\Users\Bruce\.virtualenvs\octo-computing-machine-kicSxgWi\Scripts\activate.ps1`
* Start server:
    * `python manage.py runserver 8020`
* Project and application URLs:
    * http://localhost:8020/
    * http://localhost:8020/api/v1/
    * http://localhost:8020/admin/
    * http://localhost:8020/links/
    * http://localhost:8020/links/create/

### Code changes and additions:

1. Create `templates\links\link_delete.html` template:
    ```
    {% extends 'base.html' %}

    {% block content %}

        <h1>Delete Link</h1>
        <form action="" method="post">
            {% csrf_token %}
            <p>Are you sure you want to delete Link "{{ link.url_label }}"?</p>
            <input type="submit" value="Confirm">
        </form>

    {% endblock content %}
    ```

1. Create `LinkDeleteView` view in `links\views.py`:
    ```
    from django.views.generic import DeleteView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.contrib.auth.mixins import UserPassesTestMixin
    from django.urls import reverse_lazy

    class LinkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Link
        template_name = 'links\link_delete.html'
        success_url = reverse_lazy('links:list')

        def test_func(self):
            post = self.get_object()
            return self.request.user == post.owner
    ```

1. Create `delete` route in `links\urls.py`:
    ```
    from links.views import LinkDeleteView

    app_name = 'links'
    urlpatterns = [
        ...
        path('<int:pk>/delete/', LinkDeleteView.as_view(), name='delete'),
        ...
    ]
    ```
