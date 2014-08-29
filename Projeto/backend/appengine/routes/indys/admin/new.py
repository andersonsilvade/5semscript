# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from indy_app import facade
from routes.indys import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'indys/admin/form.html')


def save(_handler, indy_id=None, **indy_properties):
    cmd = facade.save_indy_cmd(**indy_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'indy': cmd.form}

        return TemplateResponse(context, 'indys/admin/form.html')
    _handler.redirect(router.to_path(admin))

