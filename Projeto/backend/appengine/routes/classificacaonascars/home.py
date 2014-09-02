# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from classificacaonascar_app import facade
from routes.classificacaonascars import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_classificacaonascars_cmd()
    classificacaonascars = cmd()
    public_form = facade.classificacaonascar_public_form()
    classificacaonascar_public_dcts = [public_form.fill_with_model(classificacaonascar) for classificacaonascar in classificacaonascars]
    context = {'classificacaonascars': classificacaonascar_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

