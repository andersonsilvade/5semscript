# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from piloto_app.model import Piloto

class PilotoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Piloto
    _include = [Piloto.categoria, 
                Piloto.nome, 
                Piloto.equipe]


class PilotoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Piloto
    _include = [Piloto.categoria, 
                Piloto.nome, 
                Piloto.equipe]


class PilotoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Piloto
    _include = [Piloto.categoria, 
                Piloto.equipe, 
                Piloto.creation, 
                Piloto.nome]


class PilotoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Piloto
    _include = [Piloto.categoria, 
                Piloto.equipe, 
                Piloto.creation, 
                Piloto.nome]


class SavePilotoCommand(SaveCommand):
    _model_form_class = PilotoForm


class UpdatePilotoCommand(UpdateNode):
    _model_form_class = PilotoForm


class ListPilotoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListPilotoCommand, self).__init__(Piloto.query_by_creation())

