from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views import generic

from BancoApp.models import Client, Vault, Box
from BancoApp.serializers import ClientsSerializer, VaultsSerializer, BoxesSerializer

# Create your views here.

def index(request):
    num_clients = Client.objects.all().count()
    num_vaults = Vault.objects.all().count()
    num_boxes = Box.objects.all().count()

    context = {
        'num_clients': num_clients,
        'num_vaults': num_vaults,
        'num_boxes': num_boxes,
    }
    return render(request, 'index.html', context = context)


#Página web para clientes
class ClientsListView(generic.ListView):
    model = Client
    context_object_name = 'client_list'
    queryset = Client.objects.all()
    template_name = 'client_list.html'

class ClientDetailView(generic.DetailView):
    model = Client

class VaultsListView(generic.ListView):
    model = Vault
    context_object_name = 'vault_list'
    queryset = Vault.objects.all()
    template_name = 'vault_list'

class VaultDetailView(generic.DetailView):
    model = Vault

class BoxesListView(generic.ListView):
    model = Box
    context_object_name = 'box_list'
    queryset = Box.objects.all()
    template_name = 'box_list'

class BoxDetailView(generic.DetailView):
    model = Box

#API CRUD en el caso de querer poder consultar y agregar registros (no segura)
@csrf_exempt
def clientApi(request, dui = ""):
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
        client = Client.objects.get(client_dui = client_data['client_dui'])
        client_serializer = ClientsSerializer(client, data = client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Se ha actualizado el registro correctamente.", safe = True)
        return JsonResponse("Algo ha salido mal", safe = False)
    elif request.method=="DELETE":
        client = Client.objects.get(clients_dui = dui)
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
    