# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from nascar_app import facade
from routes.nascars import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_nascars_cmd()
    nascars = cmd()
    public_form = facade.nascar_public_form()
    nascar_public_dcts = [public_form.fill_with_model(nascar) for nascar in nascars]
    context = {'nascars': nascar_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

