# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from dtm_app.model import Dtm

class DtmPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Dtm
    _include = [Dtm.descricao]


class DtmForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Dtm
    _include = [Dtm.descricao]


class DtmDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Dtm
    _include = [Dtm.creation, 
                Dtm.descricao]


class DtmShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Dtm
    _include = [Dtm.creation, 
                Dtm.descricao]


class SaveDtmCommand(SaveCommand):
    _model_form_class = DtmForm


class UpdateDtmCommand(UpdateNode):
    _model_form_class = DtmForm


class ListDtmCommand(ModelSearchCommand):
    def __init__(self):
        super(ListDtmCommand, self).__init__(Dtm.query_by_creation())

