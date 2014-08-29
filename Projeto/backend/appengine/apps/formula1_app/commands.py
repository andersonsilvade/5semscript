# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from formula1_app.model import Formula1

class Formula1PublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Formula1
    _include = [Formula1.descricao]


class Formula1Form(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Formula1
    _include = [Formula1.descricao]


class Formula1DetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Formula1
    _include = [Formula1.creation, 
                Formula1.descricao]


class Formula1ShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Formula1
    _include = [Formula1.creation, 
                Formula1.descricao]


class SaveFormula1Command(SaveCommand):
    _model_form_class = Formula1Form


class UpdateFormula1Command(UpdateNode):
    _model_form_class = Formula1Form


class ListFormula1Command(ModelSearchCommand):
    def __init__(self):
        super(ListFormula1Command, self).__init__(Formula1.query_by_creation())

