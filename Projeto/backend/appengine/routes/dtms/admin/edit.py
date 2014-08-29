# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from dtm_app import facade
from routes.dtms import admin


@no_csrf
def index(dtm_id):
    dtm = facade.get_dtm_cmd(dtm_id)()
    detail_form = facade.dtm_detail_form()
    context = {'save_path': router.to_path(save, dtm_id), 'dtm': detail_form.fill_with_model(dtm)}
    return TemplateResponse(context, 'dtms/admin/form.html')


def save(_handler, dtm_id, **dtm_properties):
    cmd = facade.update_dtm_cmd(dtm_id, **dtm_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'dtm': cmd.form}

        return TemplateResponse(context, 'dtms/admin/form.html')
    _handler.redirect(router.to_path(admin))

