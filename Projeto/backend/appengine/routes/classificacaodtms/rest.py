# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from classificacaodtm_app import facade


def index():
    cmd = facade.list_classificacaodtms_cmd()
    classificacaodtm_list = cmd()
    short_form=facade.classificacaodtm_short_form()
    classificacaodtm_short = [short_form.fill_with_model(m) for m in classificacaodtm_list]
    return JsonResponse(classificacaodtm_short)


def save(**classificacaodtm_properties):
    cmd = facade.save_classificacaodtm_cmd(**classificacaodtm_properties)
    return _save_or_update_json_response(cmd)


def update(classificacaodtm_id, **classificacaodtm_properties):
    cmd = facade.update_classificacaodtm_cmd(classificacaodtm_id, **classificacaodtm_properties)
    return _save_or_update_json_response(cmd)


def delete(classificacaodtm_id):
    facade.delete_classificacaodtm_cmd(classificacaodtm_id)()


def _save_or_update_json_response(cmd):
    try:
        classificacaodtm = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.classificacaodtm_short_form()
    return JsonResponse(short_form.fill_with_model(classificacaodtm))

