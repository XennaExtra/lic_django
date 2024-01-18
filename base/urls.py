from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("lista_badan/", views.badania, name="lista_badan"),
    path("nasze_placowki/", views.placowki, name="nasze_placowki")
]