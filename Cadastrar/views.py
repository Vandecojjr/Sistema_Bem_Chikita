from django.shortcuts import render ,redirect ,get_object_or_404 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Materia_prima, Material_do_produto, Produto

prodCad = Produto

def atualizarProduto():
     for p in prodCad.objects.all():
         l_preco = []
         for m in Material_do_produto.objects.all():
             if (m.idPoduto).id == p.id:
                qt_material = m.qunat
                valorMaterial = (m.idMaterial).preco
                x = int(qt_material) * valorMaterial
                l_preco.append(x)
         if p.porcemPadrao == 'sim' or p.precoAutomatico == 'sim':
             if p.precoAutomatico == 'sim':
                if p.porcemPadrao == 'sim' and p.porcemLucro == 0:
                    p.preco = (sum(l_preco)*0.3) + sum(l_preco)
                    p.porcemLucro = 30
                    p.save()
                else:
                    p.preco = (sum(l_preco)*((p.porcemLucro)/100)) + sum(l_preco)
                    p.save()
             else:
                 if sum(l_preco) == 0:
                     p.porcemLucro = 0
                     p.save()
                 else:
                    p.porcemLucro = ((p.preco - sum(l_preco)) / sum(l_preco)) * 100
                    p.save()
                 
             
def index(request):
    return render(request, 'index.html')

def produto(request):
    if str(request.method) == 'POST':

        tratando_preco = request.POST.get('valor')
        if tratando_preco == '':
            tratando_preco = 0
        else:
            tratando_preco = tratando_preco.replace(",",".")

        tratando_porc = request.POST.get('%')
        if tratando_porc == '':
            tratando_porc = 0
        else:
            tratando_porc = tratando_porc.replace(",",".")

        novo_produto = prodCad()
        novo_produto.nome = request.POST.get('Nome')
        novo_produto.descricao = request.POST.get('descricao')
        novo_produto.preco = tratando_preco
        novo_produto.precoAutomatico = request.POST.get('precoAutomatico')
        novo_produto.porcemPadrao = request.POST.get('porcemAutomatico')
        novo_produto.porcemLucro = tratando_porc
        novo_produto.save()
    prod = {
        'produtos': prodCad.objects.all()
    }
    atualizarProduto()
    return render(request, 'produto.html', prod)

def materia_prima(request):
    if str(request.method) == 'POST':

        tratando_string = request.POST.get('valor')
        tratando_string = tratando_string.replace(",",".")

        novo_material = Materia_prima()
        novo_material.nome = request.POST.get('Nome')
        novo_material.descricao = request.POST.get('descricao')
        novo_material.u_medida = request.POST.get('u_medida')
        novo_material.preco = tratando_string
        novo_material.save()
        #Dicionario que armazena todas as informacoes da tabela (materia prima)
    Mprima = {
        'Mprima': Materia_prima.objects.all()
    }
    return render(request, 'M_prima.html',Mprima) 

def Delete_material(request, id):
    del_materal = Materia_prima.objects.get(id=id)
    del_materal.delete()
    return redirect('Mprima')


def deletar_produto(request, id):
    del_produto = prodCad.objects.get(id=id)
    del_produto.delete()
    return redirect('produto')

def editarMprima(request, item_id):

    item = Materia_prima.objects.get(id=item_id)
    context = {
        'item':item
    }
    if str(request.method) == 'POST':
        tratando_string = request.POST.get('valor')
        tratando_string = tratando_string.replace(",",".")

        item.nome = request.POST.get('Nome')
        item.descricao = request.POST.get('descricao')
        item.u_medida = request.POST.get('u_medida')
        item.preco = tratando_string
        item.save()
        return redirect('Mprima')
    return render(request, 'editar_material.html',context)

def editarProduto(request, id):

    item = prodCad.objects.get(id=id)
    context = {
        'item':item
    }
    if str(request.method) == 'POST':

        tratando_preco = request.POST.get('valor')
        if tratando_preco == '':
            tratando_preco = 0
        else:
            tratando_preco = tratando_preco.replace(",",".")

        tratando_porc = request.POST.get('%')
        if tratando_porc == '':
            tratando_porc = 0
        else:
            tratando_porc = tratando_porc.replace(",",".")

        item.nome = request.POST.get('Nome')
        item.descricao = request.POST.get('descricao')
        item.preco = tratando_preco
        item.precoAutomatico = request.POST.get('precoAutomatico')
        item.porcemPadrao = request.POST.get('porcemAutomatico')
        item.porcemLucro = tratando_porc
        item.save()
        return redirect('produto')
    
    return render(request, 'editar_produto.html',context)

@csrf_exempt
def cad_M_produto(request, id_Produto):
    produto = id_Produto
    context = {
        'Mprima': Materia_prima.objects.all(),
        'MprimaProduto': Material_do_produto.objects.all(),
        'produto': produto
    }
    if str(request.method) == 'POST':
        chave1 = request.POST.get('chave1')
        chave2 = request.POST.get('chave2')
        chave3 = int(request.POST.get('chave3'))

        novoMaterialProduto = Material_do_produto()
        novoMaterialProduto.idMaterial = Materia_prima.objects.get(id=chave2)
        novoMaterialProduto.idPoduto = prodCad.objects.get(id=chave3)
        novoMaterialProduto.qunat = chave1
        novoMaterialProduto.save()

        pro = prodCad.objects.get(id = id_Produto)
        
        x_material = list(Material_do_produto.objects.filter(idPoduto=id_Produto))
        l_preco = []
        
        for material in x_material:
            x = 0
            qt_material = material.qunat
            valorMaterial = (material.idMaterial).preco
            x = int(qt_material) * valorMaterial
            l_preco.append(x)
        '''if pro.porcemPadrao == 'sim' or pro.precoAutomatico == 'sim':
            if pro.porcemPadrao == 'sim' and pro.porcemLucro == 0:
                pro.preco = (sum(l_preco)*0.3) + sum(l_preco)
                pro.porcemLucro = 30
                pro.save()
            else:
                pro.preco = (sum(l_preco)*((pro.porcemLucro)/100)) + sum(l_preco)
                pro.save()'''
        teste = Material_do_produto.objects.all().values()
        return JsonResponse({'teste': list(teste)})
    return render(request, 'Cadastro_produto.html',context)

def sua_view(request,id_Produto,x):
    x_material = list(Material_do_produto.objects.filter(idPoduto=id_Produto))
    
    Material = {}
    
    for material in x_material:
        M = 'materia' + str(material.id)
        Mdic = {}

        qt_material = material.qunat

        nomeMaterial = (material.idMaterial).nome
        idDoMaterial = material.id

        Mdic['nome'] = nomeMaterial
        Mdic['qunat'] = qt_material
        Mdic['id'] = idDoMaterial

        Material[M] = Mdic
    Material = Material.values()
    return JsonResponse({'material': list(Material)})       

@require_http_methods(["DELETE"])
def deletarMprimaProduto(request, id):
    try:
        deletar = Material_do_produto.objects.get(id=id)
        deletar.delete()
        return JsonResponse({'message': 'Material do produto excluído com sucesso.'}, status=204)
    except Material_do_produto.DoesNotExist:
        return JsonResponse({'message': 'Material do produto não encontrado.'}, status=404)
    