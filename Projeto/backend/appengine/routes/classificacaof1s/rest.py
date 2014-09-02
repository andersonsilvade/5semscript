# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from classificacaof1_app import facade


def index():
    cmd = facade.list_classificacaof1s_cmd()
    classificacaof1_list = cmd()
    short_form=facade.classificacaof1_short_form()
    classificacaof1_short = [short_form.fill_with_model(m) for m in classificacaof1_list]
    return JsonResponse(classificacaof1_short)


def save(**classificacaof1_properties):
    cmd = facade.save_classificacaof1_cmd(**classificacaof1_properties)
    return _save_or_update_json_response(cmd)


def update(classificacaof1_id, **classificacaof1_properties):
    cmd = facade.update_classificacaof1_cmd(classificacaof1_id, **classificacaof1_properties)
    return _save_or_update_json_response(cmd)


def delete(classificacaof1_id):
    facade.delete_classificacaof1_cmd(classificacaof1_id)()


def _save_or_update_json_response(cmd):
    try:
        classificacaof1 = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.classificacaof1_short_form()
    return JsonResponse(short_form.fill_with_model(classificacaof1))

