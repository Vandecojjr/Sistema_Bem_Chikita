
$(document).ready(function () {
    // Função para abrir o modal de edição
    function abrirModalEdicao(itemID) {
        $.get('Cadastro_produto/' + itemID, function (data) {
            var modalContent = $('.modal-content');
            modalContent.html(data);
    
            // Abra o modal após preencher o conteúdo
            document.getElementById("myModal").style.display = "block";
            document.getElementById("myModal").classList.add("fade-in");
        });
    }

    // Quando o botão "Editar" é clicado, chama a função de abrir o modal de edição
    $(document).on('click', '.editar-item-btn', function () {
        var itemID = $(this).data('item-id');
        abrirModalEdicao(itemID);
    });

});