from django.urls import path  # type: ignore
from django.contrib import admin  # type: ignore
from Proj.views import ProdutoListView, ProdutoCreateView, ProdutoDetailView, ProdutoUpdateView, ProdutoDeleteView, CategoriaCreateView, CategoriaListView # type: ignore
from account.views import RegisterView,CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", RegisterView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view() , name='login'),
    path('categorias/', CategoriaListView.as_view(), name='CategoriaListView'),
    path('categorias/noadicionar/', CategoriaCreateView.as_view(), name='CategoriaCreateView'),
    path('', ProdutoListView.as_view(), name='ProdutoListView'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='ProdutoDetailView'),
    path('produto/create/', ProdutoCreateView.as_view(), name='ProdutoCreateView'),
    path('produto/edit/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='ProdutoUpdateView'),
    path('produto/delete/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='ProdutoDeleteView'),
]