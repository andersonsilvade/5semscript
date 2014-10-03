# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
from gaepermission.decorator import login_not_required
from routes.bdclassificacao import *
from routes.bdclassificacao import Classificacao
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse



@login_not_required
@no_csrf
def index(categoria):
    query = Classificacao.query(Classificacao.cat == categoria).order(-Classificacao.pon)
    pilotos = query.fetch()
    form = ClassificacaoFormTable()
    pilotos = [form.fill_with_model(piloto)for piloto in pilotos]

    editar_form_path = router.to_path(editar_form)

    for piloto in pilotos:
        piloto['edit_path'] = "%s/%s" %(editar_form_path, piloto['id'])


    if categoria == "f1":
        contexto = {'f1':pilotos}
        return TemplateResponse(contexto,'classificacaof1s/home.html')
    if categoria == "dtm":
         contexto = {'dtm':pilotos}
         return TemplateResponse(contexto,'classificacaodtms/home.html')
    if categoria == "indy":
         contexto = {'indy':pilotos}
         return TemplateResponse(contexto,'classificacaoindys/home.html')
    if categoria == "nascar":
         contexto = {'nascar':pilotos}
         return TemplateResponse(contexto,'classificacaonascars/home.html')


@no_csrf
def editar_form(piloto_id):
    piloto_id = int(piloto_id)
    pilotos = Classificacao._get_by_id(piloto_id)
    piloto_form = ClassificacaoForm()
    piloto_form.fill_with_model(pilotos)
    contexto={'salvar_path':router.to_path(editar),'pilotos':piloto_form }
    return TemplateResponse(contexto,'bdclassificacao/form.html')

def editar(**propriedades):
    classificacao_form = ClassificacaoForm(**propriedades)
    erros = classificacao_form.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar),'erros':erros,'classificacao':classificacao_form }
        return TemplateResponse(contexto,'bdclassificacao/form.html')

    else:
        classificacao=classificacao_form.fill_model()
        classificacao.put()
        return RedirectResponse(router.to_path(form))



