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


class Overview(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FunctionalModules(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TechnologyStack(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DevelopmentPipeline(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TechnicalUpdates(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Deployment(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Training(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
