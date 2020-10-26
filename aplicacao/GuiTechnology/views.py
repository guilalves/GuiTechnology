from django.http import request
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    
    dados = {
        'produtos' : produtos
    }
    return render(request,'index.html',dados)

def produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    produto_a_exibir = {
        'produto': produto
    }
    return render(request,'produtos.html', produto_a_exibir)

def buscar(request):
    
    lista_produtos = produtos = Produto.objects.all()
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_produtos = lista_produtos.filter(nome_produto__icontains=nome_a_buscar)
            
    dados = {
        'produtos': lista_produtos
    }

    return render(request, 'buscar.html', dados)