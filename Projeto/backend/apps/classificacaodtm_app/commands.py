# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from classificacaodtm_app.model import Classificacaodtm

class ClassificacaodtmPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Classificacaodtm
    _include = [Classificacaodtm.Classificacao]


class ClassificacaodtmForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Classificacaodtm
    _include = [Classificacaodtm.Classificacao]


class ClassificacaodtmDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Classificacaodtm
    _include = [Classificacaodtm.Classificacao, 
                Classificacaodtm.creation]


class ClassificacaodtmShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Classificacaodtm
    _include = [Classificacaodtm.Classificacao, 
                Classificacaodtm.creation]


class SaveClassificacaodtmCommand(SaveCommand):
    _model_form_class = ClassificacaodtmForm


class UpdateClassificacaodtmCommand(UpdateNode):
    _model_form_class = ClassificacaodtmForm


class ListClassificacaodtmCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClassificacaodtmCommand, self).__init__(Classificacaodtm.query_by_creation())

