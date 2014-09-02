# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from classificacaodtm_app import facade
from routes.classificacaodtms import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_classificacaodtms_cmd()
    classificacaodtms = cmd()
    public_form = facade.classificacaodtm_public_form()
    classificacaodtm_public_dcts = [public_form.fill_with_model(classificacaodtm) for classificacaodtm in classificacaodtms]
    context = {'classificacaodtms': classificacaodtm_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

