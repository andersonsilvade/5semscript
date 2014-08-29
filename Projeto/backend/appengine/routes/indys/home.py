# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from indy_app import facade
from routes.indys import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_indys_cmd()
    indys = cmd()
    public_form = facade.indy_public_form()
    indy_public_dcts = [public_form.fill_with_model(indy) for indy in indys]
    context = {'indys': indy_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

