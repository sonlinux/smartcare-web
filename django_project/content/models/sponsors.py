# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class Partner(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    url = models.URLField(
        _('Website URL'),
        blank=True,
        null=True
    )
    description = RichTextField(
        _('Description'),
        blank=True,
        null=True
    )
    logo = models.ImageField(
        _('Logo'),
        null=True,
        blank=True,
        upload_to='partner/logos/%Y/%m/%d'
    )

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
