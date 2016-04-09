from django.db import models


class ItemGeolocationMixin(models.Model):

    class Meta:
        abstract = True
