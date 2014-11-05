# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from piloto_app import facade
from routes.pilotos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_pilotos_cmd()
    pilotos = cmd()
    public_form = facade.piloto_public_form()
    piloto_public_dcts = [public_form.fill_with_model(piloto) for piloto in pilotos]
    context = {'pilotos': piloto_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

