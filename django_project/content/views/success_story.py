# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

from django.views.generic import TemplateView, ListView

from ..models.success_story import SuccessStory

class SuccessStoryList(ListView):
    template_name = 'content/success_stories_list.html'
    model = SuccessStory

    def get_context_data(self, **kwargs):
        context = super(SuccessStoryList, self).get_context_data(**kwargs)

        success_qs = SuccessStory.objects.filter(published=True)
        context['success_stories'] = success_qs

        return context
