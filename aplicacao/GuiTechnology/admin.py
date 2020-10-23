from django.contrib import admin
from .models import Produto

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'marca', 'preco')
    list_display_links = ('id', 'nome_produto')
    search_fields = ('id', 'nome_produto')
    list_filter = ('marca',)
    list_per_page = (6)

admin.site.register(Produto, ListandoProdutos)