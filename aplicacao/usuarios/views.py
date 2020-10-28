from django.contrib.messages.api import error
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from GuiTechnology.models import Produto

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_iguais(senha, senha2):
            messages.error(request, 'As senhas não conferem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usário já existente')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usário já existente')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    return render(request,'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
    
def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_iguais(senha, senha2):
    return senha != senha2

def dashboard(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.all()
    
        dados = {
            'produtos' : produtos
            }
        #return render(request,'index.html',dados)
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')