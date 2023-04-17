from django.db import models

# Create your models here.

class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_datebirth = models.DateField()

class Vaults(models.Model):
    vault_id = models.AutoField(primary_key=True)
    vault_serial_number = models.CharField(max_length=10)
    vault_number_of_boxes = models.IntegerField()

class Boxes(models.Model):
    box_id = models.AutoField(primary_key=True)
    box_serial_number = models.CharField(max_length=10)
    box_owner = models.CharField(max_length=500)