from django.views.generic import FormView, TemplateView
from django.db import transaction
from braces.views import FormMessagesMixin

class HomeView(TemplateView):
    template_name = 'content/home.html'
