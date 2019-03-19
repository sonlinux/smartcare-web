# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <mukomalison@gmail.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__doc__ = ''
__license__ = ''
__copyright__ = ''

from django.conf.urls import url
from .views.home import HomeView
from .views.home import AboutUsView
from .views.success_story import (
    SuccessStoryList,
    SuccessStoryDetail)


urlpatterns = [
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^about/$',
        AboutUsView.as_view(),
        name='about'),
    url(r'^success/$',
        SuccessStoryList.as_view(),
        name='success'),
    url(r'^story/(?P<story_pk>\d+)/detail/$',
        SuccessStoryDetail.as_view(),
        name='success_detail')
]
