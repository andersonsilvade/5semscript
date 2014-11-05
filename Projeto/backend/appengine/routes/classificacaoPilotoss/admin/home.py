# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaoPilotos_app import facade
from routes.classificacaoPilotoss.admin import new, edit


def delete(_handler, classificacao_pilotos_id):
    facade.delete_classificacao_pilotos_cmd(classificacao_pilotos_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_classificacao_pilotoss_cmd()
    classificacao_pilotoss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.classificacao_pilotos_short_form()

    def short_classificacao_pilotos_dict(classificacao_pilotos):
        classificacao_pilotos_dct = short_form.fill_with_model(classificacao_pilotos)
        classificacao_pilotos_dct['edit_path'] = router.to_path(edit_path, classificacao_pilotos_dct['id'])
        classificacao_pilotos_dct['delete_path'] = router.to_path(delete_path, classificacao_pilotos_dct['id'])
        return classificacao_pilotos_dct

    short_classificacao_pilotoss = [short_classificacao_pilotos_dict(classificacao_pilotos) for classificacao_pilotos in classificacao_pilotoss]
    context = {'classificacao_pilotoss': short_classificacao_pilotoss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

