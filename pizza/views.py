from django.views.generic import TemplateView, ListView, DetailView
from .models import PizzaMenu


class IndexView(TemplateView):
    template_name = "index.html"


class PizzaMenuListView(ListView):
    model = PizzaMenu
    template_name = "menu.html"
    context_object_name = "pizza_menu"

    # ordering = ["price"]


class PizzaDetailView(DetailView):
    model = PizzaMenu
    template_name = "pizza_detail.html"
    context_object_name = "pizza_detail"


class About(TemplateView):
    template_name = "about.html"
