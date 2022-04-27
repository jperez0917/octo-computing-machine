## Issue 22 - Accounts API setup
[Issue 22](https://github.com/jperez0917/octo-computing-machine/issues/22)

### Resources:

* https://github.com/django/django

### Commands, virtual environment, etc:

* Virtual environment activation:
    * Powershell: `C:\Users\Bruce\.virtualenvs\octo-computing-machine-kicSxgWi\Scripts\activate.ps1`
* Start server:
    * `python manage.py runserver 8020`
* Application URL:
    * http://localhost:8020/
    * http://localhost:8020/api/v1/
    * http://localhost:8020/admin/

### Create the `api` app:

1. Create Django `api` app:
`python manage.py startapp api`
    ```
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d----          2022-04-25    15:53                migrations
    -a---          2022-04-25    15:53              0 __init__.py
    -a---          2022-04-25    15:53             66 admin.py
    -a---          2022-04-25    15:53            144 apps.py
    -a---          2022-04-25    15:53             60 models.py
    -a---          2022-04-25    15:53             63 tests.py
    -a---          2022-04-25    15:53             66 views.py
    ```

1. Add apps to `knowledge_quest\settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'api.apps.ApiConfig',
        ...
    ]
    ```

1. Add `UserSerializer` to a new file `api\serializers.py`:
    ```
    from rest_framework import serializers

    from django.contrib.auth import get_user_model

    from accounts.models import CustomUser

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    ```

1. Add `UserViewSet` to a new file `api\views.py`:
    ```
    from rest_framework import viewsets

    from django.contrib.auth import get_user_model

    from api.serializers import UserSerializer

    class UserViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = get_user_model().objects.all()
        serializer_class = UserSerializer
    ```

1. Add route to `api\urls.py`:
    ```
    from django.urls import path
    from rest_framework.routers import DefaultRouter

    from api.views import UserViewSet

    router = DefaultRouter()
    router.register('users', UserViewSet, basename='users')

    urlpatterns = router.urls + [
        
    ]
    ```

1. Add URL routes to `knowledge_quest\urls.py`:
    ```
    urlpatterns = [
        ...
        path('api/v1/', include('api.urls')),
        path('api-auth/', include('rest_framework.urls')),
        ...
    ]
    ```

