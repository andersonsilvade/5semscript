# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from dtm_app.commands import ListDtmCommand, SaveDtmCommand, UpdateDtmCommand, \
    DtmPublicForm, DtmDetailForm, DtmShortForm


def save_dtm_cmd(**dtm_properties):
    """
    Command to save Dtm entity
    :param dtm_properties: a dict of properties to save on model
    :return: a Command that save Dtm, validating and localizing properties received as strings
    """
    return SaveDtmCommand(**dtm_properties)


def update_dtm_cmd(dtm_id, **dtm_properties):
    """
    Command to update Dtm entity with id equals 'dtm_id'
    :param dtm_properties: a dict of properties to update model
    :return: a Command that update Dtm, validating and localizing properties received as strings
    """
    return UpdateDtmCommand(dtm_id, **dtm_properties)


def list_dtms_cmd():
    """
    Command to list Dtm entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListDtmCommand()


def dtm_detail_form(**kwargs):
    """
    Function to get Dtm's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return DtmDetailForm(**kwargs)


def dtm_short_form(**kwargs):
    """
    Function to get Dtm's short form. just a subset of dtm's properties
    :param kwargs: form properties
    :return: Form
    """
    return DtmShortForm(**kwargs)

def dtm_public_form(**kwargs):
    """
    Function to get Dtm'spublic form. just a subset of dtm's properties
    :param kwargs: form properties
    :return: Form
    """
    return DtmPublicForm(**kwargs)


def get_dtm_cmd(dtm_id):
    """
    Find dtm by her id
    :param dtm_id: the dtm id
    :return: Command
    """
    return NodeSearch(dtm_id)


def delete_dtm_cmd(dtm_id):
    """
    Construct a command to delete a Dtm
    :param dtm_id: dtm's id
    :return: Command
    """
    return DeleteNode(dtm_id)

