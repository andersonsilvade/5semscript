# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from classificacaoPilotos_app import facade
from routes.classificacaoPilotoss import admin


@login_not_required
@no_csrf
def index(categoria):
    cmd = facade.list_classificacao_pilotoss_cmd()
    classificacao_pilotoss = cmd()
    public_form = facade.classificacao_pilotos_public_form()
    classificacao_pilotos_public_dcts = [public_form.fill_with_model(classificacao_pilotos) for classificacao_pilotos in classificacao_pilotoss]
    context = {'classificacao_pilotoss': classificacao_pilotos_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

