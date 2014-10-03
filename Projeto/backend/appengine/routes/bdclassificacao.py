# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from gaegraph.model import Node
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm
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

class ClassificacaoFormTable(ModelForm):
    _model_class = Classificacao
    _include = [Classificacao.pil,Classificacao.equ,Classificacao.cat,Classificacao.pon]

class ClassificacaoForm(ModelForm):
    _model_class = Classificacao
    _include = [Classificacao.pil,Classificacao.equ,Classificacao.cat,Classificacao.pon]



def salvar(**propriedades):
    classificacao_form = ClassificacaoForm(**propriedades)
    erros = classificacao_form.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar),'erros':erros,'classificacao':classificacao_form }
        return TemplateResponse(contexto,'bdclassificacao/form.html')

    else:
        classificacao=classificacao_form.fill_model()
        classificacao.put()
        return RedirectResponse(router.to_path(form))




