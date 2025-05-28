from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from datetime import datetime

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        data_internacao = request.POST.get('data_internacao')
        motivo = request.POST.get('motivo')
        leito_numero = request.POST.get('leito')
        obs = request.POST.get('obs')

        if not (nome and idade and cpf and sexo and data_internacao and motivo and leito_numero):
            return HttpResponseBadRequest("Dados incompletos")

        try:
            data_internacao_obj = datetime.strptime(
                data_internacao, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponseBadRequest("Data de internação inválida")

        return redirect('leitos:leitos')

    else:
        leito_numero = request.GET.get('leito', '')

        return render(request, 'cadastro.html', {
            'leito_numero': leito_numero,
        })
