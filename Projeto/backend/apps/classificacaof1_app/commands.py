# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from classificacaof1_app.model import Classificacaof1

class Classificacaof1PublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Classificacaof1
    _include = [Classificacaof1.Classificacao]


class Classificacaof1Form(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Classificacaof1
    _include = [Classificacaof1.Classificacao]


class Classificacaof1DetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Classificacaof1
    _include = [Classificacaof1.Classificacao, 
                Classificacaof1.creation]


class Classificacaof1ShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Classificacaof1
    _include = [Classificacaof1.Classificacao, 
                Classificacaof1.creation]


class SaveClassificacaof1Command(SaveCommand):
    _model_form_class = Classificacaof1Form


class UpdateClassificacaof1Command(UpdateNode):
    _model_form_class = Classificacaof1Form


class ListClassificacaof1Command(ModelSearchCommand):
    def __init__(self):
        super(ListClassificacaof1Command, self).__init__(Classificacaof1.query_by_creation())

