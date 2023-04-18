from django.conf.urls import url
from BancoApp import views

urlpatterns = [
    url(r'^client$', views.clientApi),
    url(r'^client/([0-9]+)$', views.clientApi),
    url(r'^vault$', views.vaultApi),
    url(r'^vault/([0-9]+)$', views.vaultApi),
    url(r'^box$', views.boxApi),
    url(r'^box/([0-9]+)$', views.boxApi)
]