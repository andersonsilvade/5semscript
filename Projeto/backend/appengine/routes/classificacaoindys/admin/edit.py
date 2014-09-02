# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaoindy_app import facade
from routes.classificacaoindys import admin


@no_csrf
def index(classificacaoindy_id):
    classificacaoindy = facade.get_classificacaoindy_cmd(classificacaoindy_id)()
    detail_form = facade.classificacaoindy_detail_form()
    context = {'save_path': router.to_path(save, classificacaoindy_id), 'classificacaoindy': detail_form.fill_with_model(classificacaoindy)}
    return TemplateResponse(context, 'classificacaoindys/admin/form.html')


def save(_handler, classificacaoindy_id, **classificacaoindy_properties):
    cmd = facade.update_classificacaoindy_cmd(classificacaoindy_id, **classificacaoindy_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacaoindy': cmd.form}

        return TemplateResponse(context, 'classificacaoindys/admin/form.html')
    _handler.redirect(router.to_path(admin))

