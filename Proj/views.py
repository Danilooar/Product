from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy # type: ignore
from .models import Produto, Categoria

class ProdutoListView(ListView):
    model = Produto
    template_name = 'Proj/products_list.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        return Produto.objects.all().select_related('categoria')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'Proj/products_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'photo', 'status','Estoque']
    template_name = 'Proj/Create_product.html'
    success_url = reverse_lazy('ProdutoListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  
        return context
    
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'Proj/create_product.html'
    context_object_name = 'categorias'


class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'Proj/categoria_create.html'
    success_url = reverse_lazy('ProdutoCreateView') 


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'categoria', 'preco', 'status', 'photo', 'descricao','Estoque']
    template_name = 'Proj/products_update.html'
    context_object_name = 'produto'
    
    def get_success_url(self):
        return reverse_lazy('ProdutoDetailView', kwargs={'pk': self.object.pk})


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'Proj/products_delete.html'
    success_url = reverse_lazy('ProdutoListView')