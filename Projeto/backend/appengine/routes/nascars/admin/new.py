# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from nascar_app import facade
from routes.nascars import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'nascars/admin/form.html')


def save(_handler, nascar_id=None, **nascar_properties):
    cmd = facade.save_nascar_cmd(**nascar_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'nascar': cmd.form}

        return TemplateResponse(context, 'nascars/admin/form.html')
    _handler.redirect(router.to_path(admin))

