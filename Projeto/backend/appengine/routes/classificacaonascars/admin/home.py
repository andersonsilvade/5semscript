# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaonascar_app import facade
from routes.classificacaonascars.admin import new, edit


def delete(_handler, classificacaonascar_id):
    facade.delete_classificacaonascar_cmd(classificacaonascar_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_classificacaonascars_cmd()
    classificacaonascars = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.classificacaonascar_short_form()

    def short_classificacaonascar_dict(classificacaonascar):
        classificacaonascar_dct = short_form.fill_with_model(classificacaonascar)
        classificacaonascar_dct['edit_path'] = router.to_path(edit_path, classificacaonascar_dct['id'])
        classificacaonascar_dct['delete_path'] = router.to_path(delete_path, classificacaonascar_dct['id'])
        return classificacaonascar_dct

    short_classificacaonascars = [short_classificacaonascar_dict(classificacaonascar) for classificacaonascar in classificacaonascars]
    context = {'classificacaonascars': short_classificacaonascars,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

