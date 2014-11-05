# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from piloto_app.commands import ListPilotoCommand, SavePilotoCommand, UpdatePilotoCommand, \
    PilotoPublicForm, PilotoDetailForm, PilotoShortForm


def save_piloto_cmd(**piloto_properties):
    """
    Command to save Piloto entity
    :param piloto_properties: a dict of properties to save on model
    :return: a Command that save Piloto, validating and localizing properties received as strings
    """
    return SavePilotoCommand(**piloto_properties)


def update_piloto_cmd(piloto_id, **piloto_properties):
    """
    Command to update Piloto entity with id equals 'piloto_id'
    :param piloto_properties: a dict of properties to update model
    :return: a Command that update Piloto, validating and localizing properties received as strings
    """
    return UpdatePilotoCommand(piloto_id, **piloto_properties)


def list_pilotos_cmd():
    """
    Command to list Piloto entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListPilotoCommand()


def piloto_detail_form(**kwargs):
    """
    Function to get Piloto's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return PilotoDetailForm(**kwargs)


def piloto_short_form(**kwargs):
    """
    Function to get Piloto's short form. just a subset of piloto's properties
    :param kwargs: form properties
    :return: Form
    """
    return PilotoShortForm(**kwargs)

def piloto_public_form(**kwargs):
    """
    Function to get Piloto'spublic form. just a subset of piloto's properties
    :param kwargs: form properties
    :return: Form
    """
    return PilotoPublicForm(**kwargs)


def get_piloto_cmd(piloto_id):
    """
    Find piloto by her id
    :param piloto_id: the piloto id
    :return: Command
    """
    return NodeSearch(piloto_id)


def delete_piloto_cmd(piloto_id):
    """
    Construct a command to delete a Piloto
    :param piloto_id: piloto's id
    :return: Command
    """
    return DeleteNode(piloto_id)

