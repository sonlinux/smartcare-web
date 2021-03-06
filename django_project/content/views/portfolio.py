# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <mukomalison@gmail.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__doc__ = ''
__license__ = ''
__copyright__ = 'Broadreach Corperation'


from django.views.generic import TemplateView


class PortfolioListingView(TemplateView):
    template_name = 'content/portfolio.html'