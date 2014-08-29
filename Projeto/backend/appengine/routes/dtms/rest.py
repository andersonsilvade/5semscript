# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from dtm_app import facade


def index():
    cmd = facade.list_dtms_cmd()
    dtm_list = cmd()
    short_form=facade.dtm_short_form()
    dtm_short = [short_form.fill_with_model(m) for m in dtm_list]
    return JsonResponse(dtm_short)


def save(**dtm_properties):
    cmd = facade.save_dtm_cmd(**dtm_properties)
    return _save_or_update_json_response(cmd)


def update(dtm_id, **dtm_properties):
    cmd = facade.update_dtm_cmd(dtm_id, **dtm_properties)
    return _save_or_update_json_response(cmd)


def delete(dtm_id):
    facade.delete_dtm_cmd(dtm_id)()


def _save_or_update_json_response(cmd):
    try:
        dtm = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.dtm_short_form()
    return JsonResponse(short_form.fill_with_model(dtm))

