from django.db import models


# Create your models here.


class Topico(models.Model):
    nome = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.nome


class Webpage(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.nome


class RegistroAcesso(models.Model):
    pagina = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return str(self.data)


class DadosForm(models.Model):
    nome = models.CharField(max_length=264, unique=True)
    sobrenome = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=264, unique=True)
    endereco = models.CharField(max_length=264, unique=True)
    pais = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=256)
    duracao = models.PositiveIntegerField()
    ano_lancamento = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    telefone = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
