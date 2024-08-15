from django.contrib import admin
from .models import Aluno
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'cpf', 'data_de_nascimento', 'imagem'] 