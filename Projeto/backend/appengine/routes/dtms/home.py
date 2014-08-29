# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from dtm_app import facade
from routes.dtms import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_dtms_cmd()
    dtms = cmd()
    public_form = facade.dtm_public_form()
    dtm_public_dcts = [public_form.fill_with_model(dtm) for dtm in dtms]
    context = {'dtms': dtm_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

