from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BancoApp.models import Clients, Vaults, Boxes
from BancoApp.serializers import ClientsSerializer, VaultsSerializer, BoxesSerializer

# Create your views here.

@csrf_exempt
def clientsApi(request, id = 0):
    if request.method=="GET":
        clients = Clients.objects.all()
        clients_serializer = ClientsSerializer(clients, many = True)
        return JsonResponse(clients_serializer.data, safe = False)
    elif request.method=="POST":
        clients_data = JSONParser().parse(request)
        clients_serializer = ClientsSerializer(data = clients_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Se ha añadido el registro correctamente.", safe = True)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="PUT":
        clients_data = JSONParser().parse(request)
        clients = Clients.objects.get(client_id = clients_data['client_id'])
        clients_serializer = ClientsSerializer(clients, data = clients_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = True)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        clients = Clients.objects.get(clients_id = id)
        clients.delete()
        return JsonResponse("Se ha borrado exitosamente", safe = False)
    
@csrf_exempt
def vaultsApi(request, id = 0):
    if request.method=="GET":
        vaults = Vaults.objects.all()
        vaults_serializer = VaultsSerializer(vaults, many = True)
        return JsonResponse(vaults_serializer.data, safe = False)
    elif request.method=="POST":
        vaults_data = JSONParser().parse(request)
        vaults_serializer = VaultsSerializer(data = vaults_data)
        if vaults_serializer.is_valid():
            vaults_serializer.save()
            return JsonResponse("Se ha añadido el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="PUT":
        vaults_data = JSONParser().parse(request)
        vaults = Vaults.objects.get(vaults_id = vaults_data['vault_id'])
        vaults_serializer = VaultsSerializer(vaults, data = vaults_data)
        if vaults_serializer.is_valid():
            vaults_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        vaults = Vaults.objects.get(vault_id = id)
        vaults.delete()
        return JsonResponse("Se ha borrado exitosamente", safe = False)
    
@csrf_exempt
def boxesApi(request, id = 0):
    if request.method=="GET":
        boxes = Boxes.objects.all()
        boxes_serializer = BoxesSerializer(boxes, many = True)
        return JsonResponse(boxes_serializer.data, safe = False)
    elif request.method=="POST":
        boxes_data = JSONParser().parse(request)
        boxes_serializer = VaultsSerializer(data = boxes_data)
        if boxes_serializer.is_valid():
            boxes_serializer.save()
            return JsonResponse("Se ha añadido el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="PUT":
        boxes_data = JSONParser().parse(request)
        boxes = Vaults.objects.get(boxes_id = boxes_data['boxes_id'])
        boxes_serializer = BoxesSerializer(boxes, data = boxes_data)
        if boxes_serializer.is_valid():
            boxes_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = False)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        boxes = Boxes.objects.get(boxes_id = id)
        boxes.delete()
        return JsonResponse("Se ha borrado exitosamente", safe = False)
    