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
from .views.under_development import UnderDevelopment
from .views.download_smartcare import DownloadFile


urlpatterns = [
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^download/$',
        DownloadFile.as_view(),
        name='download'),
    url(r'^under-development/$',
        UnderDevelopment.as_view(),
        name='under_development'),
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
