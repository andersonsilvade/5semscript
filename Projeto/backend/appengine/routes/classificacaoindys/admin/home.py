# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaoindy_app import facade
from routes.classificacaoindys.admin import new, edit


def delete(_handler, classificacaoindy_id):
    facade.delete_classificacaoindy_cmd(classificacaoindy_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_classificacaoindys_cmd()
    classificacaoindys = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.classificacaoindy_short_form()

    def short_classificacaoindy_dict(classificacaoindy):
        classificacaoindy_dct = short_form.fill_with_model(classificacaoindy)
        classificacaoindy_dct['edit_path'] = router.to_path(edit_path, classificacaoindy_dct['id'])
        classificacaoindy_dct['delete_path'] = router.to_path(delete_path, classificacaoindy_dct['id'])
        return classificacaoindy_dct

    short_classificacaoindys = [short_classificacaoindy_dict(classificacaoindy) for classificacaoindy in classificacaoindys]
    context = {'classificacaoindys': short_classificacaoindys,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

