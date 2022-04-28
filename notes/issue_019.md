## Issue 19 - User can signup, login, and logout of basic app
[Issue 19](https://github.com/jperez0917/octo-computing-machine/issues/19)

### Resources:

* https://github.com/django/django
* https://learndjango.com/tutorials/django-custom-user-model

### Commands, virtual environment, etc:

* Virtual environment activation:
    * Powershell: `C:\Users\Bruce\.virtualenvs\octo-computing-machine-kicSxgWi\Scripts\activate.ps1`
* Start server:
    * `python manage.py runserver 8020`
* Application URL:
    * http://localhost:8020/
    * http://localhost:8020/admin/

### Virtual environment:

1. Create virtual environment, or install apps into existing virtual environment:
`pipenv install django==4.0 docutils==0.18.1 djangorestframework==3.13.1`
`pip list`
    ```
    Package             Version
    ------------------- -------
    asgiref             3.5.0
    Django              4.0
    djangorestframework 3.13.1
    docutils            0.18.1
    pip                 22.0.4
    pytz                2022.1
    setuptools          61.0.0
    sqlparse            0.4.2
    tzdata              2022.1
    wheel               0.37.1
    ```

### Django project setup and `accounts` app added:

1. Create Django project:
`django-admin startproject knowledge_quest .`
    ```
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d----          2022-04-25    09:59                knowledge_quest
    d----          2022-04-25    09:52                notes
    -a---          2022-04-25    09:59            693 manage.py
    -a---          2022-04-25    09:55            211 Pipfile
    -a---          2022-04-25    09:55           2701 Pipfile.lock
    ```

1. Create `accounts` app:
`python manage.py startapp accounts`
    ```
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d----          2022-04-25    10:11                accounts
    d----          2022-04-25    10:11                knowledge_quest
    d----          2022-04-25    09:52                notes
    -a---          2022-04-25    09:59            693 manage.py
    -a---          2022-04-25    09:55            211 Pipfile
    -a---          2022-04-25    09:55           2701 Pipfile.lock
    ```

1. Test server:
`python manage.py runserver 8020`

### Set up Django to use environment variable for salting and hashing:

1. Modify `knowledge_quest\setting.py` to use environment variable `SECRET_KEY`, and set `TIME_ZONE`:
    ```
    import os

    SECRET_KEY = os.environ.get('SECRET_KEY')

    TIME_ZONE = 'America/New_York'
    ```

### Set up `accounts` app:

1. Create `CustomUser` model in `accounts\models.py`:
    ```
    from django.contrib.auth.models import AbstractUser


    class CustomUser(AbstractUser):
        pass

        def __str__(self):
            return self.username
    ```

1. Modify `knowledge_quest\setting.py`:
    ```
    INSTALLED_APPS = [
        ...    
        'accounts.apps.AccountsConfig',
        ...
    ]

    ...
    AUTH_USER_MODEL = 'accounts.CustomUser'
    ...
    ```

1. Create forms in `accounts\forms.py`:
    ```
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    from accounts.models import CustomUser

    class CustomUserCreationForm(UserCreationForm):
        
        class Meta:
            model = CustomUser
            fields = ('username', 'email')

    class CustomUserChangeForm(UserChangeForm):

        class Meta:
            model = CustomUser
            fields = ('username', 'email')
    ```

1. Modify `accounts\admin.py` to control what shows in Django Admin Page:
    ```
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from accounts.forms import CustomUserChangeForm
    from accounts.forms import CustomUserCreationForm
    from accounts.models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser
        list_display = ('email', 'username')

    admin.site.register(CustomUser, CustomUserAdmin)
    ```

1. Migrations:

    NOTE: Migrate `accounts` first since it has a `CustomUser`.

    `python manage.py makemigrations accounts`

    `python manage.py sqlmigrate accounts 0001`

    `python manage.py migrate accounts`

    `python manage.py migrate`

1. Create `superuser`:
`python manage.py createsuperuser`

### Create Django templates:

1. Create `templates` directory:
`New-Item -ItemType 'directory' -Path .\templates`

1. Create `templates/registration/` directory:
`New-Item -ItemType 'directory' -Path .\templates\registration`

1. Add `templates` directory to `knowledge_quest\settings.py`:
    ```
    TEMPLATES = [
        {
            ...
            'DIRS': [BASE_DIR / 'templates'],
            ...
        },
    ]
    ```

1. Define redirects in `knowledge_quest\settings.py`:
    ```
    LOGIN_REDIRECT_URL = 'home'
    LOGOUT_REDIRECT_URL = 'home'
    ```

1. Create `templates\registration\login.html`:
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

1. Create `templates\registration\signup.html`:
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

1. Create `templates\base.html`:
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

1. Create `templates\home.html`:
    ```
    {% extends "base.html" %}

    {% block title %}Home{% endblock %}

    {% block content %}
        {% if user.is_authenticated %}
            Hi {{ user.username|capfirst }}!
            <p><a href="{% url 'logout' %}">Log Out</a></p>
            {% else %}
            <p>You are not logged in</p>
            <a href="{% url 'login' %}">Log In</a> |
            <a href="{% url 'signup' %}">Sign Up</a>
        {% endif %}
    {% endblock %}
    ```

1. Create `SignUpView` in `accounts\views.py`:
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
    ```
    from django.urls import path

    from accounts.views import SignUpView


    urlpatterns = [
        path('signup/', SignUpView.as_view(), name='signup'),
    ]
    ```

1. Add routes to `knowledge_quest\urls.py`:
    ```
    from django.contrib import admin
    from django.urls import path, include
    from django.views.generic.base import TemplateView

    urlpatterns = [
        path('', TemplateView.as_view(template_name='home.html'), name='home'),
        path('admin/', admin.site.urls),
        path('accounts/', include('accounts.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
    ]
    ```

### Set up Admin Documentation Generator:

* https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/

1. Add `django.contrib.admindocs` to `knowledge_quest\settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'django.contrib.admindocs',
        ...
    ]
    ```

1. Add route to `knowledge_quest\settings.py`:
    ```
    urlpatterns = [
        ...
        path('admin/doc/', include('django.contrib.admindocs.urls')),
        ...
    ]
    ```



