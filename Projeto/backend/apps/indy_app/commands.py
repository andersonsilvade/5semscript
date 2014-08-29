# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from indy_app.model import Indy

class IndyPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Indy
    _include = [Indy.descricao]


class IndyForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Indy
    _include = [Indy.descricao]


class IndyDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Indy
    _include = [Indy.creation, 
                Indy.descricao]


class IndyShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Indy
    _include = [Indy.creation, 
                Indy.descricao]


class SaveIndyCommand(SaveCommand):
    _model_form_class = IndyForm


class UpdateIndyCommand(UpdateNode):
    _model_form_class = IndyForm


class ListIndyCommand(ModelSearchCommand):
    def __init__(self):
        super(ListIndyCommand, self).__init__(Indy.query_by_creation())

