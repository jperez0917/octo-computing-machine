from django.db import models
from django.urls import reverse

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
        return f'{ self.id } : {self.owner} : { self.url_label }'

    def get_absolute_url(self):
        return reverse('links:detail', args=(self.pk,))

    class Meta:
        ordering = ('-id',)


