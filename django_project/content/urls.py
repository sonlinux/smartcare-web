# coding: utf-8
from datetime import datetime


__author__ = 'Alison Mukoma <mukomalison@gmail.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__doc__ = ''
__license__ = ''
__copyright__ = ''

from django.conf.urls import url
from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home')
]
