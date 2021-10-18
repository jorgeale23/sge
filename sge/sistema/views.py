from django.shortcuts import render
from sistema.forms import *
from sistema.clases import *
from sistema.models import Electrodomestico

import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np
# Create your views here.


def index(request):
    return render(request, 'sge/index.html')


def electro_view(request):
    if request.method == 'POST':
        form = ElectrodomesticoForm(request.POST)
        form.fields['Linea'].initial = 3
        if form.is_valid():
            form.save()
        return render(request, 'sge/index.html')
    else:
        form = ElectrodomesticoForm()
        form.fields['Linea'].initial = 3
    return render(request, 'sge/electro_form.html', {'form': form})

def electro_list(request):
    electrodomestico = Electrodomestico.objects.filter(Linea=3)
    contexto = {'electrodomestico': electrodomestico}
    return render(request, 'sge/electro_list.html',contexto)


def electro_edit(request, id_electro):
    electrodomestico = Electrodomestico.objects.get(id=id_electro)
    if request.method == 'GET':
        form =ElectrodomesticoFormEdit(instance=electrodomestico)
    else:
        form = ElectrodomesticoFormEdit(request.POST,instance=electrodomestico)
        if form.is_valid():
            form.save()
        electrodomestico = Electrodomestico.objects.filter(Linea=3)
        contexto = {'electrodomestico': electrodomestico}
        return render(request, 'sge/electro_list.html', contexto)
    return render(request,'sge/electro_form.html', {'form': form})


def electro_delete(request, id_electro):
    electrodomestico = Electrodomestico.objects.get(id=id_electro)
    if request.method == 'POST':
        electrodomestico.delete()
        electrodomestico = Electrodomestico.objects.filter(Linea=3)
        contexto = {'electrodomestico': electrodomestico}
        return render(request, 'sge/electro_list.html', contexto)
    return render(request, 'sge/electro_delete.html', {'electrodomestico': electrodomestico})

def luz_view(request):
    if request.method == 'POST':
        form = LuzForm(request.POST)
        form.fields['Linea'].initial = 1
        form.fields['Marca'].initial = "i"
        form.fields['Modelo'].initial = "i"
        form.fields['Horas'].initial = -1
        if form.is_valid():
            form.save()
        return render(request, 'sge/index.html')
    else:
        form = LuzForm()
        form.fields['Linea'].initial = 1
        form.fields['Marca'].initial = "i"
        form.fields['Modelo'].initial = "i"
        form.fields['Horas'].initial = -1
    return render(request, 'sge/luz_form.html', {'form': form})


def luz_list(request):
    electrodomestico = Electrodomestico.objects.filter(Linea=1)
    contexto = {'electrodomestico': electrodomestico}
    return render(request, 'sge/luz_list.html',contexto)

def luz_edit(request, id_electro):
    electrodomestico = Electrodomestico.objects.get(id=id_electro)
    if request.method == 'GET':
        form =LuzFormEdit(instance=electrodomestico)
    else:
        form = LuzFormEdit(request.POST,instance=electrodomestico)
        if form.is_valid():
            form.save()
        electrodomestico = Electrodomestico.objects.filter(Linea=1)
        contexto = {'electrodomestico': electrodomestico}
        return render(request, 'sge/luz_list.html', contexto)
    return render(request,'sge/luz_form.html', {'form': form})

def luz_delete(request, id_electro):
    electrodomestico = Electrodomestico.objects.get(id=id_electro)
    if request.method == 'POST':
        electrodomestico.delete()
        electrodomestico = Electrodomestico.objects.filter(Linea=1)
        contexto = {'electrodomestico': electrodomestico}
        return render(request, 'sge/luz_list.html', contexto)
    return render(request, 'sge/luz_delete.html', {'electrodomestico': electrodomestico})

def climatizador_view(request):
    if request.method == 'POST':
        form = ClimatizadorForm(request.POST)
        form.fields['Linea'].initial = 2
        if form.is_valid():
            form.save()
        return render(request, 'sge/index.html')
    else:
        form = ClimatizadorForm()
        form.fields['Linea'].initial = 2
        form.fields['Horas'].initial = -1
    return render(request, 'sge/clima_form.html', {'form': form})

def clima_list(request):
    electrodomestico = Electrodomestico.objects.filter(Linea=2)
    contexto = {'electrodomestico': electrodomestico}
    return render(request, 'sge/clima_list.html',contexto)


def clima_edit(request, id_electro):
    electrodomestico = Electrodomestico.objects.get(id=id_electro)
    if request.method == 'GET':
        form =ClimaFormEdit(instance=electrodomestico)
    else:
        form = ClimaFormEdit(request.POST,instance=electrodomestico)
        if form.is_valid():
            form.save()
        electrodomestico = Electrodomestico.objects.filter(Linea=2)
        contexto = {'electrodomestico': electrodomestico}
        return render(request, 'sge/clima_list.html', contexto)
    return render(request,'sge/clima_form.html', {'form': form})


def clima_delete(request, id_electro):
    electrodomestico = Electrodomestico.objects.get(id=id_electro)
    if request.method == 'POST':
        electrodomestico.delete()
        electrodomestico = Electrodomestico.objects.filter(Linea=2)
        contexto = {'electrodomestico': electrodomestico}
        return render(request, 'sge/clima_list.html', contexto)
    return render(request, 'sge/clima_delete.html', {'electrodomestico': electrodomestico})


def horario_view(request):
    if request.method == 'POST':
        form = HoraCasaForm(request.POST)
        if form.is_valid():
            form.save()
        horacasa = HoraCasa.objects.order_by('Dia')
        contexto = {'hora': horacasa}
        return render(request, 'sge/hora_list.html', contexto)
    else:
        form = HoraCasaForm()
    return render(request, 'sge/hora_form.html', {'form': form})

def horario_list(request):
    horacasa = HoraCasa.objects.order_by('Dia')
    contexto = {'hora': horacasa}
    return render(request, 'sge/hora_list.html',contexto)

def horario_delete(request, id_horario):
    hora = HoraCasa.objects.get(id=id_horario)
    if request.method == 'POST':
        hora.delete()
        horacasa = HoraCasa.objects.order_by('Dia')
        contexto = {'hora': horacasa}
        return render(request, 'sge/hora_list.html', contexto)
    return render(request, 'sge/hora_delete.html', {'hora': hora})

def grafico(request):
    #plt.plot(range(10))


    plt.figure(figsize=(9, 3))

    grupos = ['Otros', 'Iluminacion', 'Climatizacion']

    electrodomoestico = Electrodomestico.objects.filter(Linea=3)
    Consumido = [0, 0, 0]
    for otros in electrodomoestico:
        Consumido[0] = (Consumido[0] + ((otros.Consumo * (otros.Horas / 60))) * 30)
    Consumido[0] = Consumido[0] / 1000

    h = HorasActivas()

    Consumido[1] = (h.totalhorasluz(10,2021)* 10) / 1000
    grupos[1]=str(((h.totalhorasluz(10,2021)) * 10) / 1000)

    Disponible = [0, 0, 0]
    indice = np.arange(len(grupos))

    ## Se crean las primeras barras
    plt.bar(indice, Consumido, label='Esperado')

    ## Se crean las segundas barras y se apilan sobre las primeras
   # plt.bar(indice, Disponible, label='Utilizado', bottom=Consumido)

    plt.xticks(indice, grupos)
    plt.ylabel("KW/H")
    #plt.xlabel("Grupos")
    plt.title('Consumos por linea')
    plt.legend()


    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'sge/plot.html',{'data':uri})
