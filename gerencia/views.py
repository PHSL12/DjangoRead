from django.shortcuts import render
from .models import Aluno

# Create your views here.

def index(request):
    alunos = Aluno.objects.all() # Select do django
    contexto = {
        'alunos': alunos,
    }
    return render(request, 'gerencia/index.html',contexto)

def detalhe_aluno(request, aluno_id):
    aluno_selecionado = Aluno.objects.get(id=aluno_id)
    contexto = {
        'aluno': aluno_selecionado
    }
    return render(request, 'gerencia/detalhe_aluno.html', contexto)