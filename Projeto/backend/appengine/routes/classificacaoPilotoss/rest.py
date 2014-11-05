# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from classificacaoPilotos_app import facade

@login_not_required
@no_csrf

def index():
    cmd = facade.list_classificacao_pilotoss_cmd()
    classificacao_pilotos_list = cmd()
    short_form=facade.classificacao_pilotos_short_form()
    classificacao_pilotos_short = [short_form.fill_with_model(m) for m in classificacao_pilotos_list]
    return JsonUnsecureResponse(classificacao_pilotos_short)

@login_not_required
@no_csrf

def save(**classificacao_pilotos_properties):
    cmd = facade.save_classificacao_pilotos_cmd(**classificacao_pilotos_properties)
    return _save_or_update_json_response(cmd)

@login_not_required
@no_csrf
def update(classificacao_pilotos_id, **classificacao_pilotos_properties):
    cmd = facade.update_classificacao_pilotos_cmd(classificacao_pilotos_id, **classificacao_pilotos_properties)
    return _save_or_update_json_response(cmd)

@login_not_required
@no_csrf
def delete(classificacao_pilotos_id):
    facade.delete_classificacao_pilotos_cmd(classificacao_pilotos_id)()

@login_not_required
@no_csrf
def _save_or_update_json_response(_resp, cmd):
    try:
        classificacao_pilotos = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse(cmd.errors)
    short_form=facade.classificacao_pilotos_short_form()
    return JsonUnsecureResponse(short_form.fill_with_model(classificacao_pilotos))

