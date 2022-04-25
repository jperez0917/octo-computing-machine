## Issue 21 - User can save url, url_label, notes in Links app

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
    * http://localhost:8020/api/v1/

### Set up `links` app:

1. Create `links` app:

`python manage.py startapp links`

1. Add `links.apps.LinksConfig` to `INSTALLED_APPS` in `knowledge_quest\settings.py`:
    ```
    INSTALLED_APPS = [
        ...
        'links.apps.LinksConfig',
        ...
    ]
    ```

1. Create `Link` in `links\models.py`:
    ```
    from django.db import models

    from knowledge_quest.settings import AUTH_USER_MODEL

    class Link(models.Model):
        url_label = models.CharField(
            'label for url resource',
            max_length=200,
            )
        url = models.URLField()
        notes = models.TextField(
            'notes for url resource content',
            default='',
            )
        date_created = models.DateTimeField(
            'date created',
            auto_now_add=True,
            )
        public = models.BooleanField(
            'specifies if Link is supposed to be displayed for anonymous users',
            default=False,
        )
        owner = models.ForeignKey(
            AUTH_USER_MODEL,
            related_name='links',
            on_delete=models.CASCADE,
        )

        def __str__(self):
            return f'{ self.id } : { self.url_label }'
        
        class Meta:
            ordering = ('-id',)
    ```

1. Migrations:

    `python manage.py makemigrations links`

    `python manage.py sqlmigrate links 0001`

    `python manage.py migrate links`

    `python manage.py migrate`

1. Add `LinkSerializer` to `api\serializers.py`:
    ```
    class LinkSerializer(serializers.ModelSerializer):

        class Meta:
            model = Link
            fields = ('id', 'url_label', 'url', 'public', 'owner')
    ```

1. Add `LinkViewSet` to `api\views.py`:
    ```
    from links.models import Link

    class LinkViewSet(viewsets.ModelViewSet):
        queryset = Link.objects.all()
        serializer_class = LinkSerializer
    ```

1. Add route to `api\urls.py`:
    ```
    from api.views import UserViewSet, LinkViewSet
    ...
    router.register('links', LinkViewSet, basename='links')
    ...
    ```

1. Update `serializers` in `api\serializers.py`:
    ```
    class NestedLinkSerializer(serializers.ModelSerializer):
        class Meta:
            model = Link
            fields = ('id', 'url_label', 'url', 'public')


    class NestedUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')


    class LinkSerializer(serializers.ModelSerializer):
        owner_detail = NestedUserSerializer(read_only=True, source='owner')
        class Meta:
            model = Link
            fields = ('id', 'url_label', 'url', 'public', 'owner', 'owner_detail')


    class UserSerializer(serializers.ModelSerializer):
        links_detail = NestedLinkSerializer(read_only=True, many=True, source='links')
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'links_detail')
    ```

