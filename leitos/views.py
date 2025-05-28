from django.shortcuts import render
from django.http import HttpResponse
from .models import Leito

def leitos(request):
    leitos = Leito.objects.all().order_by('numero')  
    return render(request, 'leitos.html', {'leitos': leitos})
