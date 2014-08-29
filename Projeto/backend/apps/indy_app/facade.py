# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from indy_app.commands import ListIndyCommand, SaveIndyCommand, UpdateIndyCommand, \
    IndyPublicForm, IndyDetailForm, IndyShortForm


def save_indy_cmd(**indy_properties):
    """
    Command to save Indy entity
    :param indy_properties: a dict of properties to save on model
    :return: a Command that save Indy, validating and localizing properties received as strings
    """
    return SaveIndyCommand(**indy_properties)


def update_indy_cmd(indy_id, **indy_properties):
    """
    Command to update Indy entity with id equals 'indy_id'
    :param indy_properties: a dict of properties to update model
    :return: a Command that update Indy, validating and localizing properties received as strings
    """
    return UpdateIndyCommand(indy_id, **indy_properties)


def list_indys_cmd():
    """
    Command to list Indy entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListIndyCommand()


def indy_detail_form(**kwargs):
    """
    Function to get Indy's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return IndyDetailForm(**kwargs)


def indy_short_form(**kwargs):
    """
    Function to get Indy's short form. just a subset of indy's properties
    :param kwargs: form properties
    :return: Form
    """
    return IndyShortForm(**kwargs)

def indy_public_form(**kwargs):
    """
    Function to get Indy'spublic form. just a subset of indy's properties
    :param kwargs: form properties
    :return: Form
    """
    return IndyPublicForm(**kwargs)


def get_indy_cmd(indy_id):
    """
    Find indy by her id
    :param indy_id: the indy id
    :return: Command
    """
    return NodeSearch(indy_id)


def delete_indy_cmd(indy_id):
    """
    Construct a command to delete a Indy
    :param indy_id: indy's id
    :return: Command
    """
    return DeleteNode(indy_id)

