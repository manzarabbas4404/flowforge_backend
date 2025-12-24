from django.db import models


class ActiveProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)
