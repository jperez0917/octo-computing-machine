## Issue 31 - User can use Django create template
[Issue 31](https://github.com/jperez0917/octo-computing-machine/issues/31)

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
    * http://localhost:8020/links/1/

### Code changes and additions:

1. Create `templates\links\link_create.html` template:
    ```
    {% extends 'base.html' %}

    {% block content %}

        <h1>New Link</h1>
        <form action="" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Save">
        </form>

    {% endblock content %}
    ```

1. Create `templates\links\link_detail.html` template:
    ```
    {% extends 'base.html' %}

    {% block content %}

        <div>
            <a href="{{ link.url }}" target="_blank">{{ link.url_label }}</a>
            <p>{{ link.id }} : {{ link.public }} : {{ link.notes }}</p>
        </div>

        {% if user == link.owner %}
            <p><a href="#">+ Edit Blog Post</a></p>
            <p><a href="#">+ Delete Blog Post</a></p>
            {% comment %} <p><a href="{% url 'posts:edit' post.pk %}">+ Edit Blog Post</a></p> {% endcomment %}
            {% comment %} <p><a href="{% url 'posts:delete' post.pk %}">+ Delete Blog Post</a></p> {% endcomment %}
        {% endif %}

    {% endblock content %}
    ```

1. Create `LinkCreateView` and `LinkDetailView` in `links\views.py`:
    ```
    from django.views.generic import CreateView, DetailView

    from links.models import Link

    class LinkCreateView(CreateView):
        model = Link
        template_name = 'links\link_create.html'
        fields = ('url', 'url_label', 'notes', 'public', 'owner')

    class LinkDetailView(DetailView):
        model = Link
        template_name = 'links\link_detail.html'
    ```

1. Add `create` and `detail` routes to `links\urls.py`:
    ```
    from links.views import LinkCreateView, LinkDetailView

    app_name = 'links'
    urlpatterns = [
        ...
        path('create/', LinkCreateView.as_view(), name='create'),
        path('<int:pk>/', LinkDetailView.as_view(), name='detail'),
        ...
    ]
    ```

1. Add `get_absolute_url` to `Link` in `links\models.py`:
```
class Link(models.Model):
    ...
    def get_absolute_url(self):
        return reverse('links:detail', args=(self.pk,))
    ...
```


