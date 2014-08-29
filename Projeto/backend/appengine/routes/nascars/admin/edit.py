# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from nascar_app import facade
from routes.nascars import admin


@no_csrf
def index(nascar_id):
    nascar = facade.get_nascar_cmd(nascar_id)()
    detail_form = facade.nascar_detail_form()
    context = {'save_path': router.to_path(save, nascar_id), 'nascar': detail_form.fill_with_model(nascar)}
    return TemplateResponse(context, 'nascars/admin/form.html')


def save(_handler, nascar_id, **nascar_properties):
    cmd = facade.update_nascar_cmd(nascar_id, **nascar_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'nascar': cmd.form}

        return TemplateResponse(context, 'nascars/admin/form.html')
    _handler.redirect(router.to_path(admin))

