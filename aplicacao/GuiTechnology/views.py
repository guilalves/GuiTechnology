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
