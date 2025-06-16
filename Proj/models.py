from django.db import models # type: ignore

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    Estoque = models.FloatField()
    status = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='products/',blank=True, null=True)
    descricao = models.TextField(null=True, blank=True)
    
    
    
    def __str__(self):
        return self.nome
