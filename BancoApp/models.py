from django.db import models
from django.urls import reverse

# Create your models here.

class Client(models.Model):
    client_dui = models.CharField(max_length=10, primary_key=True)
    client_name = models.CharField(max_length=100)
    client_datebirth = models.DateField()
    class Meta:
        ordering = ['client_dui']
    def __str__(self):
        return f'{self.client_dui} ({self.client_name})'

class Vault(models.Model):
    vault_id = models.AutoField(primary_key=True)
    vault_serial_number = models.CharField(max_length=10)
    vault_number_of_boxes = models.IntegerField()
    class Meta:
        ordering = ['vault_serial_number']
    def __str__(self):
        return self.vault_serial_number

class Box(models.Model):
    box_id = models.AutoField(primary_key=True)
    box_serial_number = models.CharField(max_length=10)
    box_vault = models.ForeignKey(Vault, on_delete = models.CASCADE)
    box_owner = models.ForeignKey(Client, on_delete = models.CASCADE)
    class Meta:
        ordering = ['box_serial_number']
    def __str__(self):
        return self.box_serial_number