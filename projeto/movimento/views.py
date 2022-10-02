from django.shortcuts import render, redirect
from .models import Movimentacao
# Create your views here.
def home(request):
    movimentacoes = Movimentacao.objects.all()
    return render(request, 'home.html', {"movimentacoes": movimentacoes})
    

def salvar(request):
    tipo = request.POST.get("tipo")
    data_inicio = request.POST.get("data_inicio")
    data_fim = request.POST.get("data_fim")
    
    
    Movimentacao.objects.create(
        tipo=tipo,
        data_inicio=data_inicio,
        data_fim=data_fim,
    )
    movimentacoes = Movimentacao.objects.all()
    return render(request,"home.html", {"movimentacoes":movimentacoes})
    
def editar(request, id):
    movimentacao= Movimentacao.objects.get(id=id)
    return render(request, "update_m.html", {"movimentacao":movimentacao})

def update(request, id):
    tipo = request.POST.get("tipo")
    data_inicio = request.POST.get("data_inicio")
    data_fim = request.POST.get("data_fim")
   
    movimentacao = Movimentacao.objects.get(id=id)
    movimentacao.tipo = tipo
    movimentacao.data_inicio = data_inicio
    movimentacao.data_fim = data_fim
    movimentacao.save()
    return redirect(home)
    
def delete(request, id):
    movimentacao= Movimentacao.objects.get(id=id)
    movimentacao.delete()
    return redirect(home)
    
    
    