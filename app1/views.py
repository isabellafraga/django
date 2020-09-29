

# def index(request):
#    return HttpResponse("Hello World!")
from django.shortcuts import render
from app1.models import RegistroAcesso
from .forms import FormName, ModelForm


def index(request):
    return render(request, 'app1/index.html')

def calc(request):
    return render(request, 'app1/calc.html')

def help(request):
    return render(request, 'app1/help.html')

def sp(request):
    return render(request, 'app1/sp.html')

def registros(request):
    lista_paginas = RegistroAcesso.objects.order_by('data')
    dict_lista2 = {"lista_acessos": lista_paginas}
    return render(request, 'app1/registros.html', dict_lista2)

def form_name(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
           print("Os campos estão corretos")
           print("Nome: " + form.cleaned_data['nome'])
           print("Email: " + form.cleaned_data['email'])
           print("Texto: " + form.cleaned_data['texto'])

    return render(request, 'app1/form.html', {"form": form})


def users(request):
    form = ModelForm()

    if request.method == "POST":
        form = ModelForm(request.POST)
        if form.is_valid():
            print("cadastrado: " + form.cleaned_data['nome'])
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'app1/modelform.html', {'form': form})

