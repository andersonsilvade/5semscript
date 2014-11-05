# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from classificacaoPilotos_app.model import ClassificacaoPilotos

class ClassificacaoPilotosPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = ClassificacaoPilotos
    _include = [ClassificacaoPilotos.categoria, 
                ClassificacaoPilotos.equipe, 
                ClassificacaoPilotos.pontos, 
                ClassificacaoPilotos.texto, 
                ClassificacaoPilotos.pilotos]


class ClassificacaoPilotosForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = ClassificacaoPilotos
    _include = [ClassificacaoPilotos.categoria, 
                ClassificacaoPilotos.equipe, 
                ClassificacaoPilotos.pontos, 
                ClassificacaoPilotos.texto, 
                ClassificacaoPilotos.pilotos]


class ClassificacaoPilotosDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = ClassificacaoPilotos
    _include = [ClassificacaoPilotos.categoria, 
                ClassificacaoPilotos.creation, 
                ClassificacaoPilotos.pilotos, 
                ClassificacaoPilotos.texto, 
                ClassificacaoPilotos.pontos, 
                ClassificacaoPilotos.equipe]


class ClassificacaoPilotosShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = ClassificacaoPilotos
    _include = [ClassificacaoPilotos.categoria, 
                ClassificacaoPilotos.creation, 
                ClassificacaoPilotos.pilotos, 
                ClassificacaoPilotos.texto, 
                ClassificacaoPilotos.pontos, 
                ClassificacaoPilotos.equipe]


class SaveClassificacaoPilotosCommand(SaveCommand):
    _model_form_class = ClassificacaoPilotosForm


class UpdateClassificacaoPilotosCommand(UpdateNode):
    _model_form_class = ClassificacaoPilotosForm


class ListClassificacaoPilotosCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClassificacaoPilotosCommand, self).__init__(ClassificacaoPilotos.query_by_creation())

