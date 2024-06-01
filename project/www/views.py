from django.shortcuts import render, get_object_or_404
from .models import Marka, Typ, Osprzęt, Model
from .forms import MarkaForm, TypForm, OsprzętForm, ModelForm
from django.http import HttpResponseRedirect
Marki = Marka.objects.all()
Typy = Typ.objects.all()
Osprzęty = Osprzęt.objects.all()
Modele = Model.objects.all()


def index(request):
    marki = Marka.objects.all()
    typy = Typ.objects.all()
    osprzety = Osprzęt.objects.all()
    modele = Model.objects.all()
    return render(request, 'www/index.html', {
        'Marki': marki,
        'Typy': typy,
        'Osprzęty': osprzety,
        'Modele': modele
    })

def bootstrap(request):

    return render(request, 'www/bootstrap.html', {
        'Modele': Modele
        })


def detail_Marka(request, pk):
    Marka = get_object_or_404(Marka, pk=pk)
    return render(request, 'www/detail-Marka.html', {
        'Marka':Marka,
        'pk':pk
    })

def detail_Typ(request, pk):
    Typ = get_object_or_404(Typ, pk)
    return render(request, 'www/detail-Typ.html',{
        'Typ':Typ,
        'pk':pk
    })

def detail_Osprzęt(request, pk):
    Osprzęt = get_object_or_404(Osprzęt, pk)
    return render(request, 'www/deatil-Osprzęt.html',{
        'Osprzęt':Osprzęt,
        'pk':pk
    })

def detail_Model(request, pk):
    Model = get_object_or_404(Model, pk)
    return render(request, 'www/deatil-Model.html',{
        'Model':Model,
        'pk':pk
    })

def Marki_lista(request):
    return render(request, 'www/Modele.html',{
        'Modele':Modele
    })

def Typy_lista(request):
    return render(request, 'www/Typy.html',{
        'Typy':Typy
    })

def Osprzęty_lista(request):
    return render(request, 'www/Osprzęty.html',{
        'Osprzęt':Osprzęt
    })

def Modele_lista(request):
    return render(request, 'www/Modele.html',{
        'Modele':Modele
    })


def dodaj_Marka(request):
    if request.method == 'POST':
        form = MarkaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = MarkaForm()

    return render(request, 'www/dodaj-Marka.html', {'form': form})

def dodaj_Typ(request):
    if request.method == 'POST':
        form = TypForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = MarkaForm()

    return render(request, 'www/dodaj-Typ.html', {'form': form})

def dodaj_Osprzęt(request):
    if request.method == 'POST':
        form = OsprzętForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = MarkaForm()

    return render(request, 'www/dodaj-Osprzęt.html', {'form': form})

def dodaj_Model(request):
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = MarkaForm()

    return render(request, 'www/dodaj-Model.html', {'form': form})

def zapisano(request):
    return render(request, 'www/zapisano.html')
