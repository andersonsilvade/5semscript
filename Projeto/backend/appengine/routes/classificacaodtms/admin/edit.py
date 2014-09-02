# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaodtm_app import facade
from routes.classificacaodtms import admin


@no_csrf
def index(classificacaodtm_id):
    classificacaodtm = facade.get_classificacaodtm_cmd(classificacaodtm_id)()
    detail_form = facade.classificacaodtm_detail_form()
    context = {'save_path': router.to_path(save, classificacaodtm_id), 'classificacaodtm': detail_form.fill_with_model(classificacaodtm)}
    return TemplateResponse(context, 'classificacaodtms/admin/form.html')


def save(_handler, classificacaodtm_id, **classificacaodtm_properties):
    cmd = facade.update_classificacaodtm_cmd(classificacaodtm_id, **classificacaodtm_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'classificacaodtm': cmd.form}

        return TemplateResponse(context, 'classificacaodtms/admin/form.html')
    _handler.redirect(router.to_path(admin))

