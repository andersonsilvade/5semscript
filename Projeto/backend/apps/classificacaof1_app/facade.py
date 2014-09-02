# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from classificacaof1_app.commands import ListClassificacaof1Command, SaveClassificacaof1Command, UpdateClassificacaof1Command, \
    Classificacaof1PublicForm, Classificacaof1DetailForm, Classificacaof1ShortForm


def save_classificacaof1_cmd(**classificacaof1_properties):
    """
    Command to save Classificacaof1 entity
    :param classificacaof1_properties: a dict of properties to save on model
    :return: a Command that save Classificacaof1, validating and localizing properties received as strings
    """
    return SaveClassificacaof1Command(**classificacaof1_properties)


def update_classificacaof1_cmd(classificacaof1_id, **classificacaof1_properties):
    """
    Command to update Classificacaof1 entity with id equals 'classificacaof1_id'
    :param classificacaof1_properties: a dict of properties to update model
    :return: a Command that update Classificacaof1, validating and localizing properties received as strings
    """
    return UpdateClassificacaof1Command(classificacaof1_id, **classificacaof1_properties)


def list_classificacaof1s_cmd():
    """
    Command to list Classificacaof1 entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListClassificacaof1Command()


def classificacaof1_detail_form(**kwargs):
    """
    Function to get Classificacaof1's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return Classificacaof1DetailForm(**kwargs)


def classificacaof1_short_form(**kwargs):
    """
    Function to get Classificacaof1's short form. just a subset of classificacaof1's properties
    :param kwargs: form properties
    :return: Form
    """
    return Classificacaof1ShortForm(**kwargs)

def classificacaof1_public_form(**kwargs):
    """
    Function to get Classificacaof1'spublic form. just a subset of classificacaof1's properties
    :param kwargs: form properties
    :return: Form
    """
    return Classificacaof1PublicForm(**kwargs)


def get_classificacaof1_cmd(classificacaof1_id):
    """
    Find classificacaof1 by her id
    :param classificacaof1_id: the classificacaof1 id
    :return: Command
    """
    return NodeSearch(classificacaof1_id)


def delete_classificacaof1_cmd(classificacaof1_id):
    """
    Construct a command to delete a Classificacaof1
    :param classificacaof1_id: classificacaof1's id
    :return: Command
    """
    return DeleteNode(classificacaof1_id)

