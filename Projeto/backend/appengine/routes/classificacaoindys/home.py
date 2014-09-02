# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from classificacaoindy_app import facade
from routes.classificacaoindys import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_classificacaoindys_cmd()
    classificacaoindys = cmd()
    public_form = facade.classificacaoindy_public_form()
    classificacaoindy_public_dcts = [public_form.fill_with_model(classificacaoindy) for classificacaoindy in classificacaoindys]
    context = {'classificacaoindys': classificacaoindy_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

