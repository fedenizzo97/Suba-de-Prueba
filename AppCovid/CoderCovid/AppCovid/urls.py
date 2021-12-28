from django.urls import path

from AppCovid import views

urlpatterns=[

    path("inicio", views.inicio),

    path("Guantes", views.Guantes),

    path("Barbijos", views.Barbijos),

    path("Oximetros",views.Oximetros),




]