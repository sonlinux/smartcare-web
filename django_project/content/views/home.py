# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'


from django.views.generic import TemplateView

from ..models.aboutus import AboutUs, Foreword


class HomeView(TemplateView):
    template_name = 'content/home.html'


class AboutUsView(TemplateView):
    template_name = 'content/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)

        aboutus_qs = AboutUs.objects.get(active=True)
        foreword_qs = Foreword.objects.get(active=True)
        context['aboutus'] = aboutus_qs
        context['foreword'] = foreword_qs

        return context