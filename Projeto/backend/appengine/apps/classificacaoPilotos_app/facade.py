# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from classificacaoPilotos_app.commands import ListClassificacaoPilotosCommand, SaveClassificacaoPilotosCommand, UpdateClassificacaoPilotosCommand, \
    ClassificacaoPilotosPublicForm, ClassificacaoPilotosDetailForm, ClassificacaoPilotosShortForm


def save_classificacao_pilotos_cmd(**classificacao_pilotos_properties):
    """
    Command to save ClassificacaoPilotos entity
    :param classificacao_pilotos_properties: a dict of properties to save on model
    :return: a Command that save ClassificacaoPilotos, validating and localizing properties received as strings
    """
    return SaveClassificacaoPilotosCommand(**classificacao_pilotos_properties)


def update_classificacao_pilotos_cmd(classificacao_pilotos_id, **classificacao_pilotos_properties):
    """
    Command to update ClassificacaoPilotos entity with id equals 'classificacao_pilotos_id'
    :param classificacao_pilotos_properties: a dict of properties to update model
    :return: a Command that update ClassificacaoPilotos, validating and localizing properties received as strings
    """
    return UpdateClassificacaoPilotosCommand(classificacao_pilotos_id, **classificacao_pilotos_properties)


def list_classificacao_pilotoss_cmd():
    """
    Command to list ClassificacaoPilotos entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListClassificacaoPilotosCommand()


def classificacao_pilotos_detail_form(**kwargs):
    """
    Function to get ClassificacaoPilotos's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaoPilotosDetailForm(**kwargs)


def classificacao_pilotos_short_form(**kwargs):
    """
    Function to get ClassificacaoPilotos's short form. just a subset of classificacao_pilotos's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaoPilotosShortForm(**kwargs)

def classificacao_pilotos_public_form(**kwargs):
    """
    Function to get ClassificacaoPilotos'spublic form. just a subset of classificacao_pilotos's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaoPilotosPublicForm(**kwargs)


def get_classificacao_pilotos_cmd(classificacao_pilotos_id):
    """
    Find classificacao_pilotos by her id
    :param classificacao_pilotos_id: the classificacao_pilotos id
    :return: Command
    """
    return NodeSearch(classificacao_pilotos_id)


def delete_classificacao_pilotos_cmd(classificacao_pilotos_id):
    """
    Construct a command to delete a ClassificacaoPilotos
    :param classificacao_pilotos_id: classificacao_pilotos's id
    :return: Command
    """
    return DeleteNode(classificacao_pilotos_id)

