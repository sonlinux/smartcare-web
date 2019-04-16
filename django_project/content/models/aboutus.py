__author__ = 'Alison Mukoma <mukomalison@gmail>'
__license__ = 'GPL'
__doc__ = 'Database design for the content data content.'

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    title = models.CharField(
        _('About Us title'),
        max_length=255,
    )

    content = RichTextField(default='')

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us Entries'

    def __str__(self):
        return self.title

class Foreword(models.Model):
    title = models.CharField(
        _('Foreword title'),
        max_length=255,
    )

    content = RichTextField(default='')

    owner = models.CharField(
        _('Foreword by'),
        max_length=255,
        blank=True,
        null=True
    )

    photo = models.ImageField(
        _('Owner\'s Picture'),
        upload_to='photos/',
        blank=True,
        null=True
    )

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Foreword'
        verbose_name_plural = 'Foreword Entries'

    def __str__(self):
        return '%s by %s' % (self.title, self.owner)

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

class Team(models.Model):

    name = models.CharField(
            _("Member Name"),
            max_length=350,
            null=True,
            blank=True,
    )

    title = models.CharField(
        _("Title/Position"),
        max_length=350,
        null=True,
        blank=True
    )

    content = RichTextField(default='')

    photo = models.ImageField(
        _('Picture'),
        upload_to='team_pics/',
        blank=True,
        null=True
    )
    
    facebook = models.CharField(
        _("Facebook URL"),
        max_length=350,
        null=True,
        blank=True,
    )

    twitter = models.CharField(
        _("Twitter URL"),
        max_length=350,
        null=True,
        blank=True,
    )

    linkedin = models.CharField(
        _("Linkedin Profile"),
        max_length=350,
        null=True,
        blank=True,
    )
    
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
