# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from pilotos2_app.model import Pilotos2

class Pilotos2PublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Pilotos2
    _include = [Pilotos2.categoria, 
                Pilotos2.nome, 
                Pilotos2.ponto, 
                Pilotos2.equipe]


class Pilotos2Form(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Pilotos2
    _include = [Pilotos2.categoria, 
                Pilotos2.nome, 
                Pilotos2.ponto, 
                Pilotos2.equipe]


class Pilotos2DetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Pilotos2
    _include = [Pilotos2.categoria, 
                Pilotos2.equipe, 
                Pilotos2.creation, 
                Pilotos2.ponto, 
                Pilotos2.nome]


class Pilotos2ShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Pilotos2
    _include = [Pilotos2.categoria, 
                Pilotos2.equipe, 
                Pilotos2.creation, 
                Pilotos2.ponto, 
                Pilotos2.nome]


class SavePilotos2Command(SaveCommand):
    _model_form_class = Pilotos2Form


class UpdatePilotos2Command(UpdateNode):
    _model_form_class = Pilotos2Form


class ListPilotos2Command(ModelSearchCommand):
    def __init__(self):
        super(ListPilotos2Command, self).__init__(Pilotos2.query_by_creation())

