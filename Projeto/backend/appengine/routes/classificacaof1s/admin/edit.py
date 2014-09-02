# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaof1_app import facade
from routes.classificacaof1s import admin


@no_csrf
def index(classificacaof1_id):
    classificacaof1 = facade.get_classificacaof1_cmd(classificacaof1_id)()
    detail_form = facade.classificacaof1_detail_form()
    context = {'save_path': router.to_path(save, classificacaof1_id), 'classificacaof1': detail_form.fill_with_model(classificacaof1)}
    return TemplateResponse(context, 'classificacaof1s/admin/form.html')


def save(_handler, classificacaof1_id, **classificacaof1_properties):
    cmd = facade.update_classificacaof1_cmd(classificacaof1_id, **classificacaof1_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacaof1': cmd.form}

        return TemplateResponse(context, 'classificacaof1s/admin/form.html')
    _handler.redirect(router.to_path(admin))

