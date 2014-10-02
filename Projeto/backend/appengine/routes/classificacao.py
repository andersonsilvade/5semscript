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





