## Issue 39 - User can edit their Links
[Issue 36](https://github.com/jperez0917/octo-computing-machine/issues/36)

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

1. Create `templates\links\link_edit.html` template:
    ```
    {% extends 'base.html' %}

    {% block content %}

        <h1>Edit a Link</h1>
        <form action="" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Save">
        </form>

    {% endblock content %}
    ```

1. Create `LinkEditView` view in `links\views.py`:
```
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class LinkEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Link
    template_name = 'links\link_edit.html'
    fields = ('url', 'url_label', 'notes', 'public')

    def test_func(self):
        link = self.get_object()
        return self.request.user == link.owner
```

1. Add `edit` route to `links\urls.py`:
    ```
    from links.views import LinkEditView

    app_name = 'links'
    urlpatterns = [
        ...
        path('<int:pk>/edit/', LinkEditView.as_view(), name='edit'),
        ...
    ]
    ```