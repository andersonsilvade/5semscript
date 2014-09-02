# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from classificacaonascar_app import facade


def index():
    cmd = facade.list_classificacaonascars_cmd()
    classificacaonascar_list = cmd()
    short_form=facade.classificacaonascar_short_form()
    classificacaonascar_short = [short_form.fill_with_model(m) for m in classificacaonascar_list]
    return JsonResponse(classificacaonascar_short)


def save(**classificacaonascar_properties):
    cmd = facade.save_classificacaonascar_cmd(**classificacaonascar_properties)
    return _save_or_update_json_response(cmd)


def update(classificacaonascar_id, **classificacaonascar_properties):
    cmd = facade.update_classificacaonascar_cmd(classificacaonascar_id, **classificacaonascar_properties)
    return _save_or_update_json_response(cmd)


def delete(classificacaonascar_id):
    facade.delete_classificacaonascar_cmd(classificacaonascar_id)()


def _save_or_update_json_response(cmd):
    try:
        classificacaonascar = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.classificacaonascar_short_form()
    return JsonResponse(short_form.fill_with_model(classificacaonascar))

