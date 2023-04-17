from django.conf.urls import url
from BancoApp import views

urlpatterns = [
    url(r'^clients$', views.clientsApi),
    url(r'^clients/([0-9]+)$', views.clientsApi),
    url(r'^vaults$', views.vaultsApi),
    url(r'^vaults/([0-9]+)$', views.vaultsApi),
    url(r'^boxes$', views.boxesApi),
    url(r'^boxes/([0-9]+)$', views.boxesApi)
]