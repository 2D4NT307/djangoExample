from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("client_dui", "client_name", "client_datebirth")

@admin.register(Vault)
class VaultsAdmin(admin.ModelAdmin):
    list_display = ("vault_serial_number", "vault_number_of_boxes")

@admin.register(Box)
class BoxesAdmin(admin.ModelAdmin):
    list_display = ("box_serial_number", "box_owner")

#admin.site.register(Vaults)
#admin.site.register(Boxes)