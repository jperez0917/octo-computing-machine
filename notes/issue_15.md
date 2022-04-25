## Project Setup

### Resources:

* https://github.com/django/django
* https://docs.djangoproject.com/en/4.0/intro/tutorial01/
* https://learndjango.com/tutorials/django-custom-user-model

### Commands, virtual environment, etc:

* Virtual environment activation:
    * Powershell: `C:\Users\Bruce\.virtualenvs\octo-computing-machine-kicSxgWi\Scripts\activate.ps1`
* Start server:
    * `python manage.py runserver 8040`
* Application URL:
    * http://localhost:8040/
    * http://localhost:8040/admin/

### Create virtual environment and install apps:

1. Create virtual environment and add a couple apps:
`pipenv install django==4.0 docutils==0.18.1 djangorestframework==3.13.1`

### Start the project:
1. Create Django Project:
`django-admin startproject knowledge_quest .`

1. Create accounts app:
`python manage.py startapp accounts`

1. Test server:
`python manage.py runserver 8040`

### Code additions and modifications:

* [Django Best Practices: Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)

1. Modify `links_project/settings.py`:
    NOTE: Setting up access to environment variable.
    ```
    import os
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TIME_ZONE = 'America/New_York'
    ```

1. Add `'accounts.app.AccountsConfig'` and `AUTH_USER_MODEL = 'accounts.CustomUser'` to `knowledge_quest.settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'accounts.apps.AccountsConfig',
        ...
    ]

    AUTH_USER_MODEL = 'accounts.CustomUser'
    ```

1. Add `CustomUser` to `accounts\models.py`:
    * https://github.com/django/django/blob/main/django/contrib/auth/models.py
    ```
    from django.contrib.auth.models import AbstractUser

    class CustomUser(AbstractUser):
        pass

        def __str__(self):
            return self.username
    ```

1. Create `accounts\forms.py`:
    * https://github.com/django/django/blob/main/django/contrib/auth/forms.py
    NOTE: `fields` specifies fields used in user signup page.
    ```
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    from accounts.models import CustomUser


    class CustomUserCreationForm(UserCreationForm):

        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name')

    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name')
    ```

1. Modify `accounts\admin.py`:
* https://github.com/django/django/blob/main/django/contrib/auth/admin.py
NOTE: `list_display` affects which fields are shown in user managemant page of Django Admin Panel.
    ```
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

    from accounts.models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ['email', 'username', 'last_name']

    admin.site.register(CustomUser, CustomUserAdmin)
    ```

1. Make migrations:
`python manage.py makemigrations accounts`

1. Verify migrations:
`python manage.py sqlmigrate accounts 0001`

1. Perform migrations:
`python manage.py migrate accounts`
`python manage.py migrate`

1. Create `superuser`:
`python manage.py createsuperuser`

### Set up Admin Documentation Generator:

* https://docs.djangoproject.com/en/3.2/ref/contrib/admin/admindocs/

1. Add `django.contrib.admindocs` to `links_project/settings.py`:
    * https://github.com/django/django/tree/main/django/contrib/admindocs
    ```
    INSTALLED_APPS = [
        ...
        'django.contrib.admindocs',
        ...
    ]
    ```

1. Add `path('admin/doc/', include('django.contrib.admindocs.urls'))` to `knowledge_quest/urls.py`:
    NOTE: Ensure the added path is above the 'admin/' route.
    ```
    from django.urls import include
    urlpatterns = [
        ...
        path('admin/doc/', include('django.contrib.admindocs.urls')),
        path('admin/', admin.site.urls),,
        ...
    ]
    ```

### Add `signup`, `login`, and `logout` functionality:

1. Add templates location directory to `knowledge_quest/settings.py`:
    ```
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'],
            ...
        },
    ]
    ```

1. Add login redirects to `knowledge_quest/settings.py`:
    ```
    LOGIN_REDIRECT_URL = 'home'
    LOGOUT_REDIRECT_URL = 'home'
    ```

1. Create `templates` and `registration` directories:
`New-Item -ItemType 'directory' -Path .\templates`
`New-Item -ItemType 'directory' -Path .\templates\registration`

1. Create the `base.html` template:
`code .\templates\base.html`
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

1. Create the `home.html` template:
`code .\templates\home.html`
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

1. Create the `login.html` template:
`code .\templates\registration\login.html`
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

1. Create the `signup.html` template:
`code .\templates\registration\signup.html`
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

1. Add user account routes to `knowledge_quest/urls.py`:
* https://github.com/django/django/blob/main/django/views/generic/base.py
    ```
    from django.views.generic.base import TemplateView

    urlpatterns = [
        ...
        path('', TemplateView.as_view(template_name='home.html'), name='home'),
        ...
        path('accounts/', include('accounts.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
        ...
    ]
    ```

1. Create `SignUpView` in `accounts\views.py`:
NOTE: `form_class` specifies which form is used.
`code .\accounts\views.py`
    ```
    from django.urls import reverse_lazy

    from django.views.generic.edit import CreateView

    from accounts.forms import CustomUserCreationForm

    class SignUpView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'registration/signup.html'
    ```

1. Create `accounts\urls.py`:
`code .\accounts\urls.py`
    ```
    from django.urls import path

    from accounts.views import SignUpView

    app_name = 'accounts'
    urlpatterns = [
        path('signup/', SignUpView.as_view(), name='signup'),
    ]
    ```

