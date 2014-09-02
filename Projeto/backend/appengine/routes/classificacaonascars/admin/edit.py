# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaonascar_app import facade
from routes.classificacaonascars import admin


@no_csrf
def index(classificacaonascar_id):
    classificacaonascar = facade.get_classificacaonascar_cmd(classificacaonascar_id)()
    detail_form = facade.classificacaonascar_detail_form()
    context = {'save_path': router.to_path(save, classificacaonascar_id), 'classificacaonascar': detail_form.fill_with_model(classificacaonascar)}
    return TemplateResponse(context, 'classificacaonascars/admin/form.html')


def save(_handler, classificacaonascar_id, **classificacaonascar_properties):
    cmd = facade.update_classificacaonascar_cmd(classificacaonascar_id, **classificacaonascar_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacaonascar': cmd.form}

        return TemplateResponse(context, 'classificacaonascars/admin/form.html')
    _handler.redirect(router.to_path(admin))

