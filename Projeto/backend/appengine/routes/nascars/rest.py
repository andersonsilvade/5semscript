# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from nascar_app import facade


def index():
    cmd = facade.list_nascars_cmd()
    nascar_list = cmd()
    short_form=facade.nascar_short_form()
    nascar_short = [short_form.fill_with_model(m) for m in nascar_list]
    return JsonResponse(nascar_short)


def save(**nascar_properties):
    cmd = facade.save_nascar_cmd(**nascar_properties)
    return _save_or_update_json_response(cmd)


def update(nascar_id, **nascar_properties):
    cmd = facade.update_nascar_cmd(nascar_id, **nascar_properties)
    return _save_or_update_json_response(cmd)


def delete(nascar_id):
    facade.delete_nascar_cmd(nascar_id)()


def _save_or_update_json_response(cmd):
    try:
        nascar = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.nascar_short_form()
    return JsonResponse(short_form.fill_with_model(nascar))

