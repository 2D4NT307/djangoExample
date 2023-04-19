from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('clients/', views.ClientsListView.as_view(), name = "clients"),
    path('vaults/', views.VaultsListView.as_view(), name = "vaults"),
    path('boxes/', views.BoxesListView.as_view(), name = "boxes"),
    path('clients/<str:pk>', views.ClientDetailView.as_view(), name='client-detail'),
    path('vaults/<int:pk>', views.VaultDetailView.as_view(), name='vault-detail'),
    path('boxes/<int:pk>', views.BoxDetailView.as_view(), name='box-detail'),
]