# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

import random
from django.views.generic import TemplateView

from ..models.aboutus import AboutUs, Foreword
from ..models.success_story import SuccessStory
from ..models.sponsors import Partner


class HomeView(TemplateView):
    template_name = 'content/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        success_qs = SuccessStory.objects.filter(published=True)[:3]
        context['recent_stories'] = success_qs

        partner_qs = Partner.objects.all()
        partner_list = list(partner_qs)
        try:
            random_four = list(random.sample(partner_list, len(partner_list)))
        except:
            random_four = []
        context['partners'] = random_four
        try:
            foreword_qs = Foreword.objects.get(active=True)
        except:
            foreword_qs = ''
        context['foreword'] = foreword_qs

        return context


class AboutUsView(TemplateView):
    template_name = 'content/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        try:
            aboutus_qs = AboutUs.objects.get(active=True)
            foreword_qs = Foreword.objects.get(active=True)
        except:
            aboutus_qs = ''
            foreword_qs = ''
        foreword_qs = Foreword.objects.get(active=True)
        context['aboutus'] = aboutus_qs
        context['foreword'] = foreword_qs

        return context
