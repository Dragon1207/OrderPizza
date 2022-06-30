from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Sum
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .models import Order, PizzaMenu


class HomeView(TemplateView):
    template_name = "home.html"


class PizzaMenuListView(ListView):
    model = PizzaMenu
    template_name = "menu.html"
    context_object_name = "pizza_menu"


class PizzaDetailView(DetailView):
    model = PizzaMenu
    template_name = "pizza_detail.html"
    context_object_name = "pizza_detail"


class CartListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "cart.html"
    context_object_name = "cart"

    # queryset filter to get only the logged user objects
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


    def get_context_data(self, **kwargs):
        if self.request.user.is_active == True:
            # Call the base implementation first to get a context
            context = super().get_context_data(**kwargs)
            # Add in a QuerySet to count all orders and total price filtered by user and completed=False
            context["total_pr"] = Order.objects.filter(
                customer=self.request.user, completed=False
            ).aggregate(Sum("total_price"))
            return context


class About(TemplateView):
    template_name = "about.html"


class LoginView(LoginView):
    template_name = "login.html"


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = "create.html"
    fields = ["product", "quantity"]
    success_url = reverse_lazy("cart")

    def form_valid(self, form):
        obj = form.save(commit=False)

        obj.customer = self.request.user
        obj.total_price = obj.get_item_cost()

        obj.save()
        return super().form_valid(form)


def contextData(request):
    if not request.user.is_authenticated:
        return JsonResponse([], safe=False)
    elif request.user.is_active == True:
        orders_count = Order.objects.filter(
            customer=request.user, completed=False
        ).count()
        data = {
            "orders_count": orders_count,
        }
        return JsonResponse(data, safe=False)