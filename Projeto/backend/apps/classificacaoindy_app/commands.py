# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from classificacaoindy_app.model import Classificacaoindy

class ClassificacaoindyPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Classificacaoindy
    _include = [Classificacaoindy.Classificacao]


class ClassificacaoindyForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Classificacaoindy
    _include = [Classificacaoindy.Classificacao]


class ClassificacaoindyDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Classificacaoindy
    _include = [Classificacaoindy.Classificacao, 
                Classificacaoindy.creation]


class ClassificacaoindyShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Classificacaoindy
    _include = [Classificacaoindy.Classificacao, 
                Classificacaoindy.creation]


class SaveClassificacaoindyCommand(SaveCommand):
    _model_form_class = ClassificacaoindyForm


class UpdateClassificacaoindyCommand(UpdateNode):
    _model_form_class = ClassificacaoindyForm


class ListClassificacaoindyCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClassificacaoindyCommand, self).__init__(Classificacaoindy.query_by_creation())

