from django.contrib import admin # type: ignore


from django.contrib import admin # type: ignore
from .models import Produto, Categoria

admin.site.register(Produto)
admin.site.register(Categoria)
