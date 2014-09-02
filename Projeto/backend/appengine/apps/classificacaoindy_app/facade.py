# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from classificacaoindy_app.commands import ListClassificacaoindyCommand, SaveClassificacaoindyCommand, UpdateClassificacaoindyCommand, \
    ClassificacaoindyPublicForm, ClassificacaoindyDetailForm, ClassificacaoindyShortForm


def save_classificacaoindy_cmd(**classificacaoindy_properties):
    """
    Command to save Classificacaoindy entity
    :param classificacaoindy_properties: a dict of properties to save on model
    :return: a Command that save Classificacaoindy, validating and localizing properties received as strings
    """
    return SaveClassificacaoindyCommand(**classificacaoindy_properties)


def update_classificacaoindy_cmd(classificacaoindy_id, **classificacaoindy_properties):
    """
    Command to update Classificacaoindy entity with id equals 'classificacaoindy_id'
    :param classificacaoindy_properties: a dict of properties to update model
    :return: a Command that update Classificacaoindy, validating and localizing properties received as strings
    """
    return UpdateClassificacaoindyCommand(classificacaoindy_id, **classificacaoindy_properties)


def list_classificacaoindys_cmd():
    """
    Command to list Classificacaoindy entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListClassificacaoindyCommand()


def classificacaoindy_detail_form(**kwargs):
    """
    Function to get Classificacaoindy's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaoindyDetailForm(**kwargs)


def classificacaoindy_short_form(**kwargs):
    """
    Function to get Classificacaoindy's short form. just a subset of classificacaoindy's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaoindyShortForm(**kwargs)

def classificacaoindy_public_form(**kwargs):
    """
    Function to get Classificacaoindy'spublic form. just a subset of classificacaoindy's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaoindyPublicForm(**kwargs)


def get_classificacaoindy_cmd(classificacaoindy_id):
    """
    Find classificacaoindy by her id
    :param classificacaoindy_id: the classificacaoindy id
    :return: Command
    """
    return NodeSearch(classificacaoindy_id)


def delete_classificacaoindy_cmd(classificacaoindy_id):
    """
    Construct a command to delete a Classificacaoindy
    :param classificacaoindy_id: classificacaoindy's id
    :return: Command
    """
    return DeleteNode(classificacaoindy_id)

