# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from indy_app import facade
from routes.indys import admin


@no_csrf
def index(indy_id):
    indy = facade.get_indy_cmd(indy_id)()
    detail_form = facade.indy_detail_form()
    context = {'save_path': router.to_path(save, indy_id), 'indy': detail_form.fill_with_model(indy)}
    return TemplateResponse(context, 'indys/admin/form.html')


def save(_handler, indy_id, **indy_properties):
    cmd = facade.update_indy_cmd(indy_id, **indy_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'indy': cmd.form}

        return TemplateResponse(context, 'indys/admin/form.html')
    _handler.redirect(router.to_path(admin))

