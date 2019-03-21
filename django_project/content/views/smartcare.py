# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

from django.views.generic import TemplateView


class OverviewView(TemplateView):
    template_name = 'content/overview.html'



class FunctionalModulesView(TemplateView):
    template_name = 'content/functional_modules.html'



class TechnologyStackView(TemplateView):
    template_name = 'content/technology_stack.html'



class DevelopmentPipelineView(TemplateView):
    template_name = 'content/development_pipeline.html'



class TechnicalUpdatesView(TemplateView):
    template_name = 'content/technical_updates.html'



class DeploymentView(TemplateView):
    template_name = 'content/deployment.html'



class TrainingView(TemplateView):
    template_name = 'content/training.html'
