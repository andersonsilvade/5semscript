# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaof1_app import facade
from routes.classificacaof1s.admin import new, edit


def delete(_handler, classificacaof1_id):
    facade.delete_classificacaof1_cmd(classificacaof1_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_classificacaof1s_cmd()
    classificacaof1s = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.classificacaof1_short_form()

    def short_classificacaof1_dict(classificacaof1):
        classificacaof1_dct = short_form.fill_with_model(classificacaof1)
        classificacaof1_dct['edit_path'] = router.to_path(edit_path, classificacaof1_dct['id'])
        classificacaof1_dct['delete_path'] = router.to_path(delete_path, classificacaof1_dct['id'])
        return classificacaof1_dct

    short_classificacaof1s = [short_classificacaof1_dict(classificacaof1) for classificacaof1 in classificacaof1s]
    context = {'classificacaof1s': short_classificacaof1s,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

