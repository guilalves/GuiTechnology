from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    produtos = {
        1:'Suporte para notebook',
        2:'MousePad',
        3:'Cabo HDMI',
        4:'Adaptador de VGA'
    }
    dados = {
        'nome_dos_produtos' : produtos
    }
    return render(request,'index.html',dados)

def produto(request):
    return render(request,'produtos.html')