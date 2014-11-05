# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.tools.devappserver2.request_rewriter import _ignore_response_headers_rewriter
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from piloto_app import facade
@login_not_required
@no_csrf
def index():
    cmd = facade.list_pilotos_cmd()
    piloto_list = cmd()
    short_form=facade.piloto_short_form()
    piloto_short = [short_form.fill_with_model(m) for m in piloto_list]
    return JsonUnsecureResponse(piloto_short)

@login_not_required
@no_csrf
def save(_resp,**piloto_properties):
    cmd = facade.save_piloto_cmd(**piloto_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_not_required
@no_csrf
def update(_resp,piloto_id, **piloto_properties):
    cmd = facade.update_piloto_cmd(piloto_id, **piloto_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_not_required
@no_csrf
def delete(piloto_id):
    facade.delete_piloto_cmd(piloto_id)()

@login_not_required
@no_csrf
def _save_or_update_json_response(_resp,cmd):
    try:
        piloto = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse( cmd.errors)
    short_form=facade.piloto_short_form()
    return JsonUnsecureResponse(short_form.fill_with_model(piloto))

