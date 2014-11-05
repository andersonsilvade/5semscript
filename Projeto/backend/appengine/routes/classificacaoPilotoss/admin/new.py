# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaoPilotos_app import facade
from routes.classificacaoPilotoss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'classificacaoPilotoss/admin/form.html')


def save(_handler, classificacao_pilotos_id=None, **classificacao_pilotos_properties):
    cmd = facade.save_classificacao_pilotos_cmd(**classificacao_pilotos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacao_pilotos': cmd.form}

        return TemplateResponse(context, 'classificacaoPilotoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

