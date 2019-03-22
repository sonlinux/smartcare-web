# coding: utf-8
from datetime import datetime


__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'


from ..models.success_story import SuccessStory
from ..models.category import Category

from django.views.generic import TemplateView

from ..models.sponsors import Partner

class SponsorPartnerView(TemplateView):
    template_name = 'content/sponsor_partner_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorPartnerView, self).get_context_data(**kwargs)
        try:
            sponsorship_stories_qs = SuccessStory.objects.filter(published=True)[:4]
            orgnanisation_qs = Partner.objects.all()
        except:
            sponsorship_stories_qs = ''
            orgnanisation_qs = ''

        context['sponsor_stories'] = sponsorship_stories_qs
        context['orgs'] = orgnanisation_qs

        return context

