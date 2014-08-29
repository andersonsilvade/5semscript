# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from indy_app import facade


def index():
    cmd = facade.list_indys_cmd()
    indy_list = cmd()
    short_form=facade.indy_short_form()
    indy_short = [short_form.fill_with_model(m) for m in indy_list]
    return JsonResponse(indy_short)


def save(**indy_properties):
    cmd = facade.save_indy_cmd(**indy_properties)
    return _save_or_update_json_response(cmd)


def update(indy_id, **indy_properties):
    cmd = facade.update_indy_cmd(indy_id, **indy_properties)
    return _save_or_update_json_response(cmd)


def delete(indy_id):
    facade.delete_indy_cmd(indy_id)()


def _save_or_update_json_response(cmd):
    try:
        indy = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.indy_short_form()
    return JsonResponse(short_form.fill_with_model(indy))

