# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from piloto_app import facade
from routes.pilotos import admin


@no_csrf
def index(piloto_id):
    piloto = facade.get_piloto_cmd(piloto_id)()
    detail_form = facade.piloto_detail_form()
    context = {'save_path': router.to_path(save, piloto_id), 'piloto': detail_form.fill_with_model(piloto)}
    return TemplateResponse(context, 'pilotos/admin/form.html')


def save(_handler, piloto_id, **piloto_properties):
    cmd = facade.update_piloto_cmd(piloto_id, **piloto_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'piloto': cmd.form}

        return TemplateResponse(context, 'pilotos/admin/form.html')
    _handler.redirect(router.to_path(admin))

