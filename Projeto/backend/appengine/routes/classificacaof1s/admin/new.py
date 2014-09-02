# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaof1_app import facade
from routes.classificacaof1s import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'classificacaof1s/admin/form.html')


def save(_handler, classificacaof1_id=None, **classificacaof1_properties):
    cmd = facade.save_classificacaof1_cmd(**classificacaof1_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacaof1': cmd.form}

        return TemplateResponse(context, 'classificacaof1s/admin/form.html')
    _handler.redirect(router.to_path(admin))

