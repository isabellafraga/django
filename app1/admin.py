from django.contrib import admin
from .models import Topico, Webpage, RegistroAcesso, DadosForm, Filme, Cliente


class FilmeAdmin(admin.ModelAdmin):
    fields = ['ano_lancamento', 'titulo', 'duracao']
    search_fields = ['titulo', 'ano_lancamento']
    list_filter = ['ano_lancamento', 'titulo', 'duracao']
    list_display = ['ano_lancamento', 'titulo', 'duracao']


# Register your models here.
admin.site.register(Topico)
admin.site.register(Webpage)
admin.site.register(RegistroAcesso)
admin.site.register(DadosForm)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Cliente)
