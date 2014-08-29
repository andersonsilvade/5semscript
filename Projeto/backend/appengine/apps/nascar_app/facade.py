# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from nascar_app.commands import ListNascarCommand, SaveNascarCommand, UpdateNascarCommand, \
    NascarPublicForm, NascarDetailForm, NascarShortForm


def save_nascar_cmd(**nascar_properties):
    """
    Command to save Nascar entity
    :param nascar_properties: a dict of properties to save on model
    :return: a Command that save Nascar, validating and localizing properties received as strings
    """
    return SaveNascarCommand(**nascar_properties)


def update_nascar_cmd(nascar_id, **nascar_properties):
    """
    Command to update Nascar entity with id equals 'nascar_id'
    :param nascar_properties: a dict of properties to update model
    :return: a Command that update Nascar, validating and localizing properties received as strings
    """
    return UpdateNascarCommand(nascar_id, **nascar_properties)


def list_nascars_cmd():
    """
    Command to list Nascar entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListNascarCommand()


def nascar_detail_form(**kwargs):
    """
    Function to get Nascar's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return NascarDetailForm(**kwargs)


def nascar_short_form(**kwargs):
    """
    Function to get Nascar's short form. just a subset of nascar's properties
    :param kwargs: form properties
    :return: Form
    """
    return NascarShortForm(**kwargs)

def nascar_public_form(**kwargs):
    """
    Function to get Nascar'spublic form. just a subset of nascar's properties
    :param kwargs: form properties
    :return: Form
    """
    return NascarPublicForm(**kwargs)


def get_nascar_cmd(nascar_id):
    """
    Find nascar by her id
    :param nascar_id: the nascar id
    :return: Command
    """
    return NodeSearch(nascar_id)


def delete_nascar_cmd(nascar_id):
    """
    Construct a command to delete a Nascar
    :param nascar_id: nascar's id
    :return: Command
    """
    return DeleteNode(nascar_id)

