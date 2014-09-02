# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from classificacaodtm_app import facade
from routes.classificacaodtms.admin import new, edit


def delete(_handler, classificacaodtm_id):
    facade.delete_classificacaodtm_cmd(classificacaodtm_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_classificacaodtms_cmd()
    classificacaodtms = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.classificacaodtm_short_form()

    def short_classificacaodtm_dict(classificacaodtm):
        classificacaodtm_dct = short_form.fill_with_model(classificacaodtm)
        classificacaodtm_dct['edit_path'] = router.to_path(edit_path, classificacaodtm_dct['id'])
        classificacaodtm_dct['delete_path'] = router.to_path(delete_path, classificacaodtm_dct['id'])
        return classificacaodtm_dct

    short_classificacaodtms = [short_classificacaodtm_dict(classificacaodtm) for classificacaodtm in classificacaodtms]
    context = {'classificacaodtms': short_classificacaodtms,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

