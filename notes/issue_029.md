## Issue 29 - User can view list of Links on some page
[Issue 29](https://github.com/jperez0917/octo-computing-machine/issues/29)

### Resources:

* https://github.com/django/django
* https://learndjango.com/tutorials/django-custom-user-model

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

### Code changes and additions:

1. Create `templates\links\link_list.html` template:
    ```
    {% extends 'base.html' %}

    {% block content %}

        {% for link in link_list %}
            <div>
                <a href="{{ link.url }}">{{ link.url_label }}</a>
                <p>{{ link.owner }} : {{ link.public }}</p>
                <p>{{ link.id }} : {{ link.notes }}</p>
            </div>
        {% endfor %}

    {% endblock content %}
    ```

1. Add `LinkListView` to `links\views.py`:
    ```
    from django.views.generic import ListView

    from links.models import Link

    class LinkListView(ListView):
        model = Link
        template_name = 'links/link_list.html'
    ```

1. Add `list` route to `links\urls.py`:
    ```
    from django.urls import path

    from links.views import LinkListView

    app_name = 'links'
    urlpatterns = [
        path('', LinkListView.as_view(), name='list')
    ]
    ```

1. Add `links` route to `knowledge_quest\settings.py`:
    ```
    urlpatterns = [
        ...
        path('links/', include('links.urls')),
        ...
    ]
    ```

