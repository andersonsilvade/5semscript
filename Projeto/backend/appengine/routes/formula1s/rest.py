# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from formula1_app import facade


def index():
    cmd = facade.list_formula1s_cmd()
    formula1_list = cmd()
    short_form=facade.formula1_short_form()
    formula1_short = [short_form.fill_with_model(m) for m in formula1_list]
    return JsonResponse(formula1_short)


def save(**formula1_properties):
    cmd = facade.save_formula1_cmd(**formula1_properties)
    return _save_or_update_json_response(cmd)


def update(formula1_id, **formula1_properties):
    cmd = facade.update_formula1_cmd(formula1_id, **formula1_properties)
    return _save_or_update_json_response(cmd)


def delete(formula1_id):
    facade.delete_formula1_cmd(formula1_id)()


def _save_or_update_json_response(cmd):
    try:
        formula1 = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.formula1_short_form()
    return JsonResponse(short_form.fill_with_model(formula1))

