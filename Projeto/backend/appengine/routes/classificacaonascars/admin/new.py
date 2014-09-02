# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaonascar_app import facade
from routes.classificacaonascars import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'classificacaonascars/admin/form.html')


def save(_handler, classificacaonascar_id=None, **classificacaonascar_properties):
    cmd = facade.save_classificacaonascar_cmd(**classificacaonascar_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacaonascar': cmd.form}

        return TemplateResponse(context, 'classificacaonascars/admin/form.html')
    _handler.redirect(router.to_path(admin))

