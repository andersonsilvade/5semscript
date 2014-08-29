# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from nascar_app import facade
from routes.nascars.admin import new, edit


def delete(_handler, nascar_id):
    facade.delete_nascar_cmd(nascar_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_nascars_cmd()
    nascars = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.nascar_short_form()

    def short_nascar_dict(nascar):
        nascar_dct = short_form.fill_with_model(nascar)
        nascar_dct['edit_path'] = router.to_path(edit_path, nascar_dct['id'])
        nascar_dct['delete_path'] = router.to_path(delete_path, nascar_dct['id'])
        return nascar_dct

    short_nascars = [short_nascar_dict(nascar) for nascar in nascars]
    context = {'nascars': short_nascars,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

