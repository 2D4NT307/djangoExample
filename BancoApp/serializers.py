from rest_framework import serializers
from BancoApp.models import Client, Vault, Box

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_dui', 'client_name', 'client_datebirth')

class VaultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vault
        fields = ('vault_id', 'vault_serial_number', 'vault_number_of_boxes')

class BoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('box_id', 'box_serial_number', 'box_owner')