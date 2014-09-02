# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from classificacaoindy_app import facade


def index():
    cmd = facade.list_classificacaoindys_cmd()
    classificacaoindy_list = cmd()
    short_form=facade.classificacaoindy_short_form()
    classificacaoindy_short = [short_form.fill_with_model(m) for m in classificacaoindy_list]
    return JsonResponse(classificacaoindy_short)


def save(**classificacaoindy_properties):
    cmd = facade.save_classificacaoindy_cmd(**classificacaoindy_properties)
    return _save_or_update_json_response(cmd)


def update(classificacaoindy_id, **classificacaoindy_properties):
    cmd = facade.update_classificacaoindy_cmd(classificacaoindy_id, **classificacaoindy_properties)
    return _save_or_update_json_response(cmd)


def delete(classificacaoindy_id):
    facade.delete_classificacaoindy_cmd(classificacaoindy_id)()


def _save_or_update_json_response(cmd):
    try:
        classificacaoindy = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.classificacaoindy_short_form()
    return JsonResponse(short_form.fill_with_model(classificacaoindy))

