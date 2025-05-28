from django.shortcuts import render # type: ignore
from .models import Produto

def Produto_V(request):
    produtos = Produto.objects.filter(status=True)
    return render(request, 'Proj.html', {'produtos': produtos})