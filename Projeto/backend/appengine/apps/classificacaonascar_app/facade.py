# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from classificacaonascar_app.commands import ListClassificacaonascarCommand, SaveClassificacaonascarCommand, UpdateClassificacaonascarCommand, \
    ClassificacaonascarPublicForm, ClassificacaonascarDetailForm, ClassificacaonascarShortForm


def save_classificacaonascar_cmd(**classificacaonascar_properties):
    """
    Command to save Classificacaonascar entity
    :param classificacaonascar_properties: a dict of properties to save on model
    :return: a Command that save Classificacaonascar, validating and localizing properties received as strings
    """
    return SaveClassificacaonascarCommand(**classificacaonascar_properties)


def update_classificacaonascar_cmd(classificacaonascar_id, **classificacaonascar_properties):
    """
    Command to update Classificacaonascar entity with id equals 'classificacaonascar_id'
    :param classificacaonascar_properties: a dict of properties to update model
    :return: a Command that update Classificacaonascar, validating and localizing properties received as strings
    """
    return UpdateClassificacaonascarCommand(classificacaonascar_id, **classificacaonascar_properties)


def list_classificacaonascars_cmd():
    """
    Command to list Classificacaonascar entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListClassificacaonascarCommand()


def classificacaonascar_detail_form(**kwargs):
    """
    Function to get Classificacaonascar's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaonascarDetailForm(**kwargs)


def classificacaonascar_short_form(**kwargs):
    """
    Function to get Classificacaonascar's short form. just a subset of classificacaonascar's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaonascarShortForm(**kwargs)

def classificacaonascar_public_form(**kwargs):
    """
    Function to get Classificacaonascar'spublic form. just a subset of classificacaonascar's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClassificacaonascarPublicForm(**kwargs)


def get_classificacaonascar_cmd(classificacaonascar_id):
    """
    Find classificacaonascar by her id
    :param classificacaonascar_id: the classificacaonascar id
    :return: Command
    """
    return NodeSearch(classificacaonascar_id)


def delete_classificacaonascar_cmd(classificacaonascar_id):
    """
    Construct a command to delete a Classificacaonascar
    :param classificacaonascar_id: classificacaonascar's id
    :return: Command
    """
    return DeleteNode(classificacaonascar_id)

