from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, ListView, TemplateView

from .models import Order, PizzaMenu


class HomeView(TemplateView):
    template_name = "home.html"


class PizzaMenuListView(ListView):
    model = PizzaMenu
    template_name = "menu.html"
    context_object_name = "pizza_menu"

    # ordering = ["price"]


class PizzaDetailView(DetailView):
    model = PizzaMenu
    template_name = "pizza_detail.html"
    context_object_name = "pizza_detail"


class Cart(ListView):
    model = Order
    template_name = "cart.html"
    context_object_name = "cart"

    # queryset filter to get only the logged user objects
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


class About(TemplateView):
    template_name = "about.html"


class LoginView(LoginView):
    template_name = "login.html"


class LogoutView(LogoutView):
    template_name = "logout.html"
