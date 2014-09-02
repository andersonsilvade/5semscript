# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from classificacaonascar_app.model import Classificacaonascar

class ClassificacaonascarPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Classificacaonascar
    _include = [Classificacaonascar.Classificacao]


class ClassificacaonascarForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Classificacaonascar
    _include = [Classificacaonascar.Classificacao]


class ClassificacaonascarDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Classificacaonascar
    _include = [Classificacaonascar.Classificacao, 
                Classificacaonascar.creation]


class ClassificacaonascarShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Classificacaonascar
    _include = [Classificacaonascar.Classificacao, 
                Classificacaonascar.creation]


class SaveClassificacaonascarCommand(SaveCommand):
    _model_form_class = ClassificacaonascarForm


class UpdateClassificacaonascarCommand(UpdateNode):
    _model_form_class = ClassificacaonascarForm


class ListClassificacaonascarCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClassificacaonascarCommand, self).__init__(Classificacaonascar.query_by_creation())

