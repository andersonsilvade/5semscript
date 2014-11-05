# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
from gaepermission.decorator import login_not_required
from routes.bdclassificacao import *
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from tekton.gae.middleware.redirect import RedirectResponse



@login_not_required
@no_csrf
def index(categoria):

    query = Classificacao.query(Classificacao.cat == categoria).order(-Classificacao.pon)
    lista_pilotos = query.fetch()
    form = ClassificacaoFormTable()
    lista_pilotos = [form.fill_with_model(piloto) for piloto in lista_pilotos]
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for pilotos in lista_pilotos:
        pilotos['edit_path'] = '%s/%s/%s' %(editar_form_path, pilotos['id'],categoria)
        pilotos['delete_path'] = '%s/%s/%s' %(delete_path, pilotos['id'],categoria)

    contexto = {'f1':lista_pilotos}
    return TemplateResponse(contexto,'classificacaof1s/home.html')

def index_json(categoria,_resp):

    query = Classificacao.query(Classificacao.cat == categoria).order(-Classificacao.pon)
    lista_pilotos = query.fetch()
    form = ClassificacaoFormTable()
    lista_pilotos = [form.fill_with_model(piloto) for piloto in lista_pilotos]

    delete_path = router.to_path(delete)
    for pilotos in lista_pilotos:
        pilotos['edit_path'] = router.to_path(editar_form, pilotos['id'],categoria)
        pilotos['delete_path'] = router.to_path(delete, pilotos['id'],categoria)

        return JsonUnsecureResponse(lista_pilotos)


@no_csrf
def delete(piloto_id,categoria):
    chave =ndb.Key(Classificacao,int(piloto_id))
    chave.delete()
    return RedirectResponse(index,categoria)


@no_csrf
def editar_form(piloto_id,categoria):

    piloto_id = int(piloto_id)
    piloto = Classificacao.get_by_id(piloto_id)
    piloto_form = ClassificacaoForm()
    piloto_form.fill_with_model(piloto)
    contexto={'salvar_path':router.to_path(editar,piloto_id,categoria),
              'classificacao':piloto_form }
    return TemplateResponse(contexto,'bdclassificacao/form.html')

def editar(piloto_id ,categoria, **propriedades):

    piloto_id = int(piloto_id)
    pilotos = Classificacao.get_by_id(piloto_id)
    classificacao_form = ClassificacaoForm(**propriedades)
    erros = classificacao_form.validate()


    if erros:
        contexto={'salvar_path':router.to_path(salvar),'erros':erros,'classificacao':classificacao_form }
        return TemplateResponse(contexto,'bdclassificacao/form.html')

    else:
        classificacao_form.fill_model(pilotos)
        pilotos.put()
        return RedirectResponse(router.to_path(index,categoria))


