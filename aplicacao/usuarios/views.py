from django.http import request
from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == 'POST':
        print('ok')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    return render(request,'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass