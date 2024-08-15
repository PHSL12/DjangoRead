from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length = 20)
    email = models.EmailField()
    cpf = models.IntegerField()
    data_de_nascimento = models.DateField()
    imagem = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return self.nome