/**
 * Created by Anderson on 26/10/2014.
 */


$(document).ready(function(){
    var $pilotosForm = $('#pilotos-form');
    $pilotosForm.hide();
    $('#mostrar-form-btn').click(function(){
        $pilotosForm.slideToggle();

    });
    /**  variaveis input */
    var $nomeInput = $('#nomeInput');
    var $equipeInput = $('#equipeInput');
    var $pontosInput = $('#pontosInput');
    var $categoriaInput = $('#categoriaInput');
    var $textoinput = $('#textoInput');

     /**  variaveis div */
    var $nomeDiv = $('#nomeDiv');
    var $equipeDiv = $('#equipeDiv');
    var $pontosDiv = $('#pontosDiv');
    var $categoriaDiv = $('#categoriaDiv');
    var $textoDiv = $('#textoDiv');

     /**  variaveis help */
    var $helpNomeSpan = $('#help-nome');
    var $helpEquipeSpan = $('#help-equipe');
    var $helpPontosSpan = $('#help-pontos');
    var $helpCategoriaSpan = $('#help-categoria');
    var $helpTextoSpan = $('#help-texto');

    /**  variaveis outros */
    var $ajaxGif = $('#ajax-gif');
    var $salvarBtn = $('#salvar-btn');
    var $corpoTabela = $('#corpo-tabela');

    /** esconder gif*/
    $ajaxGif.hide();

    var adicionarLinha = function adicionarLinha(piloto){
         var linha = '<tr id="tr' + piloto.id + '"><td></td> <td>' + piloto.nome + '</td>' +
            '<td>' + piloto.equipe + '</td>' +
            '<td>' + piloto.pontos + '</td>' +
            '<td><button id="bt' + piloto.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';
        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr'+ piloto.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();

        $('#bt'+ piloto.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/classificacaoPilotoss/rest/delete',{'piloto_id':piloto.id}).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/classificacaoPilotoss/rest').success(function (listaDePiloto) {
        for (var i = 0; i < listaDePiloto.length; i += 1) {
            adicionarLinha(listaDePiloto[i]);
        }

    });

    $salvarBtn.click(function () {
        var piloto = {

            nome: $nomeInput.val(),
            equipe: $equipeInput.val(),
            categoria: $categoriaInput.val(),
            pontos:$pontosInput.val(),
            texto:$textoinput.val()


                   };

        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/classificacaoPilotoss/rest/save', piloto);
        promessa.success(function (piloto_do_servidor){
            adicionarLinha(piloto_do_servidor);
        });


        promessa.error(function (erros) {
            if (erros.responseJSON != null && erros.responseJSON.nome != null) {
                   $nomeDiv.addClass('has-error');
                   $helpNomeSpan.text(erros.responseJSON.nome);
                }
            if (erros.responseJSON != null && erros.responseJSON.equipe != null) {
                    $equipeDiv.addClass('has-error');
                    $helpEquipeSpan.text(erros.responseJSON.equipe);
                }

            if (erros.responseJSON != null && erros.responseJSON.categoria != null) {
                    $categoriaDiv.addClass('has-error');
                    $helpCategoriaSpan.text(erros.responseJSON.categoria);
                }
            if (erros.responseJSON != null && erros.responseJSON.pontos != null) {
                    $categoriaDiv.addClass('has-error');
                    $helpCategoriaSpan.text(erros.responseJSON.pontos);
                }



        });

        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        });
    });

});



