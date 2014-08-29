# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from formula1_app import facade
from routes.formula1s import admin


@no_csrf
def index(formula1_id):
    formula1 = facade.get_formula1_cmd(formula1_id)()
    detail_form = facade.formula1_detail_form()
    context = {'save_path': router.to_path(save, formula1_id), 'formula1': detail_form.fill_with_model(formula1)}
    return TemplateResponse(context, 'formula1s/admin/form.html')


def save(_handler, formula1_id, **formula1_properties):
    cmd = facade.update_formula1_cmd(formula1_id, **formula1_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'formula1': cmd.form}

        return TemplateResponse(context, 'formula1s/admin/form.html')
    _handler.redirect(router.to_path(admin))

