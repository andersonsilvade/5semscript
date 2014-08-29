# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from formula1_app.commands import ListFormula1Command, SaveFormula1Command, UpdateFormula1Command, \
    Formula1PublicForm, Formula1DetailForm, Formula1ShortForm


def save_formula1_cmd(**formula1_properties):
    """
    Command to save Formula1 entity
    :param formula1_properties: a dict of properties to save on model
    :return: a Command that save Formula1, validating and localizing properties received as strings
    """
    return SaveFormula1Command(**formula1_properties)


def update_formula1_cmd(formula1_id, **formula1_properties):
    """
    Command to update Formula1 entity with id equals 'formula1_id'
    :param formula1_properties: a dict of properties to update model
    :return: a Command that update Formula1, validating and localizing properties received as strings
    """
    return UpdateFormula1Command(formula1_id, **formula1_properties)


def list_formula1s_cmd():
    """
    Command to list Formula1 entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListFormula1Command()


def formula1_detail_form(**kwargs):
    """
    Function to get Formula1's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return Formula1DetailForm(**kwargs)


def formula1_short_form(**kwargs):
    """
    Function to get Formula1's short form. just a subset of formula1's properties
    :param kwargs: form properties
    :return: Form
    """
    return Formula1ShortForm(**kwargs)

def formula1_public_form(**kwargs):
    """
    Function to get Formula1'spublic form. just a subset of formula1's properties
    :param kwargs: form properties
    :return: Form
    """
    return Formula1PublicForm(**kwargs)


def get_formula1_cmd(formula1_id):
    """
    Find formula1 by her id
    :param formula1_id: the formula1 id
    :return: Command
    """
    return NodeSearch(formula1_id)


def delete_formula1_cmd(formula1_id):
    """
    Construct a command to delete a Formula1
    :param formula1_id: formula1's id
    :return: Command
    """
    return DeleteNode(formula1_id)

