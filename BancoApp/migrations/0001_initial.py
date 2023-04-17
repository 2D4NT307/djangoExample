# Generated by Django 3.2.18 on 2023-04-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxes',
            fields=[
                ('box_id', models.AutoField(primary_key=True, serialize=False)),
                ('box_serial_number', models.CharField(max_length=10)),
                ('box_owner', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('client_datebirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vaults',
            fields=[
                ('vault_id', models.AutoField(primary_key=True, serialize=False)),
                ('vault_serial_number', models.CharField(max_length=10)),
                ('vault_number_of_boxes', models.IntegerField()),
            ],
        ),
    ]
