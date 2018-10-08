from django.views.generic import TemplateView

# Create your views here.
class TopView(TemplateView):
    template_name = "main/index.html"
