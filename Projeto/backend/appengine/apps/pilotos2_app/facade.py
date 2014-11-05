# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from pilotos2_app.commands import ListPilotos2Command, SavePilotos2Command, UpdatePilotos2Command, \
    Pilotos2PublicForm, Pilotos2DetailForm, Pilotos2ShortForm


def save_pilotos2_cmd(**pilotos2_properties):
    """
    Command to save Pilotos2 entity
    :param pilotos2_properties: a dict of properties to save on model
    :return: a Command that save Pilotos2, validating and localizing properties received as strings
    """
    return SavePilotos2Command(**pilotos2_properties)


def update_pilotos2_cmd(pilotos2_id, **pilotos2_properties):
    """
    Command to update Pilotos2 entity with id equals 'pilotos2_id'
    :param pilotos2_properties: a dict of properties to update model
    :return: a Command that update Pilotos2, validating and localizing properties received as strings
    """
    return UpdatePilotos2Command(pilotos2_id, **pilotos2_properties)


def list_pilotos2s_cmd():
    """
    Command to list Pilotos2 entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListPilotos2Command()


def pilotos2_detail_form(**kwargs):
    """
    Function to get Pilotos2's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return Pilotos2DetailForm(**kwargs)


def pilotos2_short_form(**kwargs):
    """
    Function to get Pilotos2's short form. just a subset of pilotos2's properties
    :param kwargs: form properties
    :return: Form
    """
    return Pilotos2ShortForm(**kwargs)

def pilotos2_public_form(**kwargs):
    """
    Function to get Pilotos2'spublic form. just a subset of pilotos2's properties
    :param kwargs: form properties
    :return: Form
    """
    return Pilotos2PublicForm(**kwargs)


def get_pilotos2_cmd(pilotos2_id):
    """
    Find pilotos2 by her id
    :param pilotos2_id: the pilotos2 id
    :return: Command
    """
    return NodeSearch(pilotos2_id)


def delete_pilotos2_cmd(pilotos2_id):
    """
    Construct a command to delete a Pilotos2
    :param pilotos2_id: pilotos2's id
    :return: Command
    """
    return DeleteNode(pilotos2_id)

