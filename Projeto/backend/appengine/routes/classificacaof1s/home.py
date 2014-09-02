# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from classificacaof1_app import facade
from routes.classificacaof1s import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_classificacaof1s_cmd()
    classificacaof1s = cmd()
    public_form = facade.classificacaof1_public_form()
    classificacaof1_public_dcts = [public_form.fill_with_model(classificacaof1) for classificacaof1 in classificacaof1s]
    context = {'classificacaof1s': classificacaof1_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

