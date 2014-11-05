# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from piloto_app import facade
from routes.pilotos.admin import new, edit


def delete(_handler, piloto_id):
    facade.delete_piloto_cmd(piloto_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_pilotos_cmd()
    pilotos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.piloto_short_form()

    def short_piloto_dict(piloto):
        piloto_dct = short_form.fill_with_model(piloto)
        piloto_dct['edit_path'] = router.to_path(edit_path, piloto_dct['id'])
        piloto_dct['delete_path'] = router.to_path(delete_path, piloto_dct['id'])
        return piloto_dct

    short_pilotos = [short_piloto_dict(piloto) for piloto in pilotos]
    context = {'pilotos': short_pilotos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

