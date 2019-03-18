__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = 'Database design for the content data content.'

from django.db import models
from django.utils.translation import ugettext_lazy as _


class smartcare(models.Model):
    """Model to store content data."""

    code = models.CharField(
            _("Product Identifier"),
            max_length=350,
            null=True,
            blank=True,
    )

    name = models.CharField(
            _("Product Name"),
            max_length=350,
            null=True,
            blank=True,
    )

    brand = models.CharField(
            _("Brand Name"),
            max_length=350,
            null=True,
            blank=True
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Catalog Data"
        verbose_name_plural = "Catalog Data"

    def __str__(self):
        return self.name
