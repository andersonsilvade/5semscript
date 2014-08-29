# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from formula1_app import facade
from routes.formula1s import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_formula1s_cmd()
    formula1s = cmd()
    public_form = facade.formula1_public_form()
    formula1_public_dcts = [public_form.fill_with_model(formula1) for formula1 in formula1s]
    context = {'formula1s': formula1_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

