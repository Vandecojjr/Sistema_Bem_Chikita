from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto', views.produto, name='produto'),
    path('Materia_prima', views.materia_prima, name='Mprima'),
    path('deleteMaterial/<int:id>', views.Delete_material, name='deleteM'),
    path('editar_material/<int:item_id>', views.editarMprima, name='editarM'),
    path('Cadastro_produto/<int:id_Produto>', views.cad_M_produto, name='cadMproduto'),
    path('Cadastro_produto/<int:id_Produto>/<int:x>', views.sua_view, name='teste'),
    path('deletar-mprima-produto/<int:id>', views.deletarMprimaProduto),
    path('deletar-produto/<int:id>', views.deletar_produto, name='deleteP'),
    path('editar_produto/<int:id>', views.editarProduto, name='editarP'),
]
