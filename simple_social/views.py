from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class TestPage(TemplateView):
    template_name = 'simple_social/login_test.html'

class ThanksPage(TemplateView):
    template_name = 'simple_social/thanks.html'

class HomePage(TemplateView):
    template_name = 'simple_social/index.html'