# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from classificacaof1_app import facade


def index():
    cmd = facade.list_classificacaof1s_cmd()
    classificacaof1_list = cmd()
    short_form=facade.classificacaof1_short_form()
    classificacaof1_short = [short_form.fill_with_model(m) for m in classificacaof1_list]
    return JsonUnsecureResponse(classificacaof1_short)

@login_not_required
@no_csrf
def save(_resp,**classificacaof1_properties):
    cmd = facade.save_classificacaof1_cmd(**classificacaof1_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_not_required
@no_csrf
def update(_resp,classificacaof1_id, **classificacaof1_properties):
    cmd = facade.update_classificacaof1_cmd(classificacaof1_id, **classificacaof1_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_not_required
@no_csrf
def delete(classificacaof1_id):
    facade.delete_classificacaof1_cmd(classificacaof1_id)()


def _save_or_update_json_response(_resp,cmd):
    try:
        classificacaof1 = cmd()
    except CommandExecutionException:
        _resp.status_code=500
        return JsonUnsecureResponse( cmd.errors)
    short_form=facade.classificacaof1_short_form()
    return JsonUnsecureResponse(short_form.fill_with_model(classificacaof1))

