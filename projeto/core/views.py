from django.shortcuts import render, redirect
from .models import Conteiner
# Create your views here.
def home(request):
    conteiners = Conteiner.objects.all()
    return render(request, 'index.html', {"conteiners": conteiners})

def salvar(request):
    nome_cliente = request.POST.get("nome_cliente")
    num_conteiner = request.POST.get("num_conteiner")
    tipo_conteiner = request.POST.get("tipo_conteiner")
    status_conteiner = request.POST.get("status_conteiner")
    categoria_conteiner = request.POST.get("categoria_conteiner")
    
    Conteiner.objects.create(
        nome_cliente=nome_cliente,
        num_conteiner=num_conteiner,
        tipo_conteiner=tipo_conteiner,
        status_conteiner=status_conteiner,
        categoria_conteiner=categoria_conteiner
    )
    conteiners = Conteiner.objects.all()
    return render(request,"index.html", {"conteiners":conteiners})
    
def editar(request, id):
    conteiner= Conteiner.objects.get(id=id)
    return render(request, "update.html", {"conteiner":conteiner})

def update(request, id):
    nome_cliente = request.POST.get("nome_cliente")
    num_conteiner = request.POST.get("num_conteiner")
    tipo_conteiner = request.POST.get("tipo_conteiner")
    status_conteiner = request.POST.get("status_conteiner")
    categoria_conteiner = request.POST.get("categoria_conteiner")
    conteiner = Conteiner.objects.get(id=id)
    conteiner.nome_cliente = nome_cliente
    conteiner.num_conteiner = num_conteiner
    conteiner.tipo_conteiner = tipo_conteiner
    conteiner.status_conteiner = status_conteiner
    conteiner.categoria_conteiner = categoria_conteiner
    conteiner.save()
    return redirect(home)
    
def delete(request, id):
    conteiner= Conteiner.objects.get(id=id)
    conteiner.delete()
    return redirect(home)
    
    
    