# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaoPilotos_app import facade
from routes.classificacaoPilotoss import admin


@no_csrf
def index(classificacao_pilotos_id):
    classificacao_pilotos = facade.get_classificacao_pilotos_cmd(classificacao_pilotos_id)()
    detail_form = facade.classificacao_pilotos_detail_form()
    context = {'save_path': router.to_path(save, classificacao_pilotos_id), 'classificacao_pilotos': detail_form.fill_with_model(classificacao_pilotos)}
    return TemplateResponse(context, 'classificacaoPilotoss/admin/form.html')


def save(_handler, classificacao_pilotos_id, **classificacao_pilotos_properties):
    cmd = facade.update_classificacao_pilotos_cmd(classificacao_pilotos_id, **classificacao_pilotos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacao_pilotos': cmd.form}

        return TemplateResponse(context, 'classificacaoPilotoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

