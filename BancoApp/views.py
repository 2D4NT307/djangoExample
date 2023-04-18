from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BancoApp.models import Client, Vault, Box
from BancoApp.serializers import ClientsSerializer, VaultsSerializer, BoxesSerializer

# Create your views here.

@csrf_exempt
def clientApi(request, id = 0):
    if request.method=="GET":
        client = Client.objects.all()
        client_serializer = ClientsSerializer(client, many = True)
        return JsonResponse(client_serializer.data, safe = False)
    elif request.method=="POST":
        client_data = JSONParser().parse(request)
        client_serializer = ClientsSerializer(data = client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Se ha añadido el registro correctamente.", safe = True)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="PUT":
        client_data = JSONParser().parse(request)
        client = Client.objects.get(client_id = client_data['client_id'])
        client_serializer = ClientsSerializer(client, data = client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = True)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        client = Client.objects.get(clients_id = id)
        client.delete()
        return JsonResponse("Se ha borrado exitosamente", safe = False)
    
@csrf_exempt
def vaultApi(request, id = 0):
    if request.method=="GET":
        vault = Vault.objects.all()
        vault_serializer = VaultsSerializer(vault, many = True)
        return JsonResponse(vault_serializer.data, safe = False)
    elif request.method=="POST":
        vault_data = JSONParser().parse(request)
        vault_serializer = VaultsSerializer(data = vault_data)
        if vault_serializer.is_valid():
            vault_serializer.save()
            return JsonResponse("Se ha añadido el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="PUT":
        vault_data = JSONParser().parse(request)
        vault = Vault.objects.get(vaults_id = vault_data['vault_id'])
        vault_serializer = VaultsSerializer(vault, data = vault_data)
        if vault_serializer.is_valid():
            vault_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        vault = Vault.objects.get(vault_id = id)
        vault.delete()
        return JsonResponse("Se ha borrado exitosamente", safe = False)
    
@csrf_exempt
def boxApi(request, id = 0):
    if request.method=="GET":
        box = Box.objects.all()
        box_serializer = BoxesSerializer(box, many = True)
        return JsonResponse(box_serializer.data, safe = False)
    elif request.method=="POST":
        box_data = JSONParser().parse(request)
        box_serializer = VaultsSerializer(data = box_data)
        if box_serializer.is_valid():
            box_serializer.save()
            return JsonResponse("Se ha añadido el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="PUT":
        box_data = JSONParser().parse(request)
        box = Vault.objects.get(boxes_id = box_data['boxes_id'])
        box_serializer = BoxesSerializer(box, data = box_data)
        if box_serializer.is_valid():
            box_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        box = Box.objects.get(boxes_id = id)
        box.delete()
        return JsonResponse("Se ha borrado exitosamente", safe = False)
    