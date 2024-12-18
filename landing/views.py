from django.views.generic import TemplateView

# Create your views here.


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'landing/index.html'

class Coal(TemplateView):
    """
    Displays Coal gift page
    """
    template_name = 'landing/coal.html'

class NaughtyNice(TemplateView):
    """
    Displays Naughty or Nice Choice Page
    """
    template_name = 'landing/naughty_nice.html'
