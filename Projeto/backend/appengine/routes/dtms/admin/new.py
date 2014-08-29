# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from dtm_app import facade
from routes.dtms import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'dtms/admin/form.html')


def save(_handler, dtm_id=None, **dtm_properties):
    cmd = facade.save_dtm_cmd(**dtm_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'dtm': cmd.form}

        return TemplateResponse(context, 'dtms/admin/form.html')
    _handler.redirect(router.to_path(admin))

