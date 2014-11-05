# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from gaegraph.model import Node
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from tekton.gae.middleware.redirect import RedirectResponse



@no_csrf
def form():
    contexto={'salvar_path':router.to_path(salvar) }
    return TemplateResponse(contexto)

class Classificacao(Node):
    pil = ndb.StringProperty(required=True)
    equ = ndb.StringProperty(required=True)
    cat = ndb.StringProperty(required=True)
    pon = ndb.IntegerProperty(required=True)
    texto = ndb.StringProperty()

class ClassificacaoFormTable(ModelForm):
    _model_class = Classificacao
    _include = [Classificacao.pil,Classificacao.equ,Classificacao.cat,Classificacao.pon,Classificacao.texto]

class ClassificacaoForm(ModelForm):
    _model_class = Classificacao
    _include = [Classificacao.pil,Classificacao.equ,Classificacao.cat,Classificacao.pon,Classificacao.texto]



def salvar(_resp,**propriedades):
    classificacao_form = ClassificacaoForm(**propriedades)
    erros = classificacao_form.validate()
    if erros:
       _resp.status_code = 500
       return JsonUnsecureResponse(erros)
    else:
        classificacao=classificacao_form.fill_model()
        classificacao.put()
        dcp = classificacao_form.fill_with_model(classificacao)
        return JsonUnsecureResponse(dcp)




