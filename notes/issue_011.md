## Notes for Basic Django Application setup:
* [Project Board](https://github.com/jperez0917/octo-computing-machine/projects/1)
* [Issue #11](https://github.com/jperez0917/octo-computing-machine/issues/11)

### Resources:
* [Django Best Practices: Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)
* [The Django admin documentation generator](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)

### Commands, virtual environment, etc:
* Virtual environment activation:
    * Powershell: `C:\Users\Bruce\.virtualenvs\octo-computing-machine-kicSxgWi\Scripts\activate.ps1`
* Server start:
    * `python manage.py runserver 8020`
* Application links:
    * http://localhost:8020/
    * http://localhost:8020/admin/

### Virtual environment setup:

1. Create virtual environment and install `django`, `docutils`, and `djangorestframework`:
    `pipenv install django==4.0 docutils==0.18.1 djangorestframework==3.13.1`

1. Activate virtual environment:
    `C:\Users\Bruce\.virtualenvs\octo-computing-machine-kicSxgWi\Scripts\activate.ps1`

### Django Project setup:

1. Create Django project:
    `django-admin startproject knowledge_quest .`

1. Create 'users' app:
    `python manage.py startapp users`

1. Check for green rocket:
    * `python manage.py runserver 8020`
    * http://localhost:8020/

### Code Creation and Modifications:

1. Modify `knowledge_quest/settings.py` to use environment variable for `SECRET_KEY`, and set `TIME_ZONE`:
    ```
    import os

    SECRET_KEY = os.environ.get('SECRET_KEY')

    TIME_ZONE = 'America/New_York'
    ```

1. Modify `knowledge_quest/settings.py` to add `users` app information:
    ```
    INSTALLED_APPS = [
        ...
        'users.apps.UsersConfig',
        ...
    ]
    ...
    AUTH_USER_MODEL = "users.CustomUser"
    ...
    ```

1. Create `CustomUser` in `users/models.py`:
    ```
    from django.contrib.auth.models import AbstractUser

    class CustomUser(AbstractUser):
        pass

        def __str__(self):
            return self.username
    ```

1. Create and specify in `users/forms.py` which fields will be included in user creation and user change forms:
    ```
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    from .models import CustomUser

    class CustomUserCreationForm(UserCreationForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")

    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ("username", "email")
    ```

1. Modify `users/admin.py`, register the admin models with `admin.site`:
    ```
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from users.forms import CustomUserCreationForm, CustomUserChangeForm
    from users.models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ["email", "username",]

    admin.site.register(CustomUser, CustomUserAdmin)
    ```

1. Migrations, migrate `users` first since it has a `CustomUser`. Verify migrations with `sqlmigrate` option:
    `python manage.py makemigrations users`
    `python manage.py sqlmigrate users 0001`
    `python manage.py migrate users`
    `python manage.py migrate`

1. Create `superuser`:
    `python manage.py createsuperuser`

1. Set up project-level tamplates directory in `knowledge_quest/settings.py`:
    ```
    TEMPLATES = [
        {
            ...
            "DIRS": [BASE_DIR / "templates"],
            ...
        },
    ]
    ```

1. Define redirect URLs in `knowledge_quest/settings.py`:
    ```
    ...
    LOGIN_REDIRECT_URL = "home"
    LOGOUT_REDIRECT_URL = "home"
    ...
    ```

1. Create `templates/registration/login.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Log In{% endblock %}

    {% block content %}
    <h2>Log In</h2>
    <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
    </form>
    {% endblock %}
    ```

1. Create `templates/registration/signup.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Sign Up{% endblock %}

    {% block content %}
    <h2>Sign Up</h2>
    <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
    </form>
    {% endblock %}
    ```

1. Create `templates/base.html`:
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
    </head>
    <body>
        <main>
        {% block content %}
        {% endblock %}
        </main>
    </body>
    </html>
    ```

1. Create `templates/home.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Home{% endblock %}

    {% block content %}
    {% if user.is_authenticated %}
    Hi {{ user.username }}!
    <p><a href="{% url 'logout' %}">Log Out</a></p>
    {% else %}
    <p>You are not logged in</p>
    <a href="{% url 'login' %}">Log In</a> |
    <a href="{% url 'signup' %}">Sign Up</a>
    {% endif %}
    {% endblock %}
    ```

1. Modify `knowledge_quest/urls.py`:
    ```
    from django.contrib import admin
    from django.urls import path, include
    from django.views.generic.base import TemplateView

    urlpatterns = [
        path('', TemplateView.as_view(template_name='home.html'), name='home'),
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
        path('users/', include('django.contrib.auth.urls')),
    ]
    ```

1. Create `users/urls.py`:
    ```
    from django.urls import path

    from users.views import SignUpView


    urlpatterns = [
        path('signup/', SignUpView.as_view(), name='signup'),
    ]
    ```

1. Modify `users/views.py`:
    ```
    from django.urls import reverse_lazy
    from django.views.generic.edit import CreateView

    from users.forms import CustomUserCreationForm


    class SignUpView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'registration/signup.html'
    ```

### Set up Admin Documentation Generator:
* https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/

1. Add `django.contrib.admindocs` to `knowledge_quest/settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'django.contrib.admindocs',
        ...
    ]
    ```

1. Add `path('admin/doc/', include('django.contrib.admindocs.urls'))` to `knowledge_quest/urls.py`:
    ```
    urlpatterns = [
        ...
        path('admin/doc/', include('django.contrib.admindocs.urls')),
        ...
    ]
    ```
