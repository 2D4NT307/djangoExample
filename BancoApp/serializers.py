from rest_framework import serializers
from BancoApp.models import Clients, Vaults, Boxes

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('client_id', 'client_name', 'client_datebirth')

class VaultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaults
        fields = ('vault_id', 'vault_serial_number', 'vault_number_of_boxes')

class BoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxes
        fields = ('box_id', 'box_serial_number', 'box_owner')