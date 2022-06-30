from django.urls import path

from pizza.views import (
    About,
    CartListView,
    HomeView,
    LoginView,
    LogoutView,
    OrderCreateView,
    PizzaDetailView,
    PizzaMenuListView,
    contextData,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("menu/", PizzaMenuListView.as_view(), name="menu"),
    path("about/", About.as_view(), name="about"),
    path("cart/", CartListView.as_view(), name="cart"),
    path("pizza/<int:pk>/", PizzaDetailView.as_view(), name="pizza_detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("order/", OrderCreateView.as_view(), name="create"),
    path("contextdata/", contextData, name="contextData"),
]
