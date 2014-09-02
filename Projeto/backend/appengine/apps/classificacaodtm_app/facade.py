# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from classificacaodtm_app.commands import ListClassificacaodtmCommand, SaveClassificacaodtmCommand, UpdateClassificacaodtmCommand, \
    ClassificacaodtmPublicForm, ClassificacaodtmDetailForm, ClassificacaodtmShortForm


def save_classificacaodtm_cmd(**classificacaodtm_properties):
    """
    Command to save Classificacaodtm entity
    :param classificacaodtm_properties: a dict of properties to save on model
    :return: a Command that save Classificacaodtm, validating and localizing properties received as strings
    """
    return SaveClassificacaodtmCommand(**classificacaodtm_properties)


def update_classificacaodtm_cmd(classificacaodtm_id, **classificacaodtm_properties):
    """
    Command to update Classificacaodtm entity with id equals 'classificacaodtm_id'
    :param classificacaodtm_properties: a dict of properties to update model
    :return: a Command that update Classificacaodtm, validating and localizing properties received as strings
    """
    return UpdateClassificacaodtmCommand(classificacaodtm_id, **classificacaodtm_properties)


def list_classificacaodtms_cmd():
    """
    Command to list Classificacaodtm entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListClassificacaodtmCommand()


def classificacaodtm_detail_form(**kwargs):
    """
    Function to get Classificacaodtm's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaodtmDetailForm(**kwargs)


def classificacaodtm_short_form(**kwargs):
    """
    Function to get Classificacaodtm's short form. just a subset of classificacaodtm's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaodtmShortForm(**kwargs)

def classificacaodtm_public_form(**kwargs):
    """
    Function to get Classificacaodtm'spublic form. just a subset of classificacaodtm's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaodtmPublicForm(**kwargs)


def get_classificacaodtm_cmd(classificacaodtm_id):
    """
    Find classificacaodtm by her id
    :param classificacaodtm_id: the classificacaodtm id
    :return: Command
    """
    return NodeSearch(classificacaodtm_id)


def delete_classificacaodtm_cmd(classificacaodtm_id):
    """
    Construct a command to delete a Classificacaodtm
    :param classificacaodtm_id: classificacaodtm's id
    :return: Command
    """
    return DeleteNode(classificacaodtm_id)

