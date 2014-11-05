# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from piloto_app import facade
from routes.pilotos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'pilotos/admin/form.html')


def save(_handler, piloto_id=None, **piloto_properties):
    cmd = facade.save_piloto_cmd(**piloto_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'piloto': cmd.form}

        return TemplateResponse(context, 'pilotos/admin/form.html')
    _handler.redirect(router.to_path(admin))

