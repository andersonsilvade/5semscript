# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from nascar_app.model import Nascar

class NascarPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Nascar
    _include = [Nascar.descricao]


class NascarForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Nascar
    _include = [Nascar.descricao]


class NascarDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Nascar
    _include = [Nascar.creation, 
                Nascar.descricao]


class NascarShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Nascar
    _include = [Nascar.creation, 
                Nascar.descricao]


class SaveNascarCommand(SaveCommand):
    _model_form_class = NascarForm


class UpdateNascarCommand(UpdateNode):
    _model_form_class = NascarForm


class ListNascarCommand(ModelSearchCommand):
    def __init__(self):
        super(ListNascarCommand, self).__init__(Nascar.query_by_creation())

