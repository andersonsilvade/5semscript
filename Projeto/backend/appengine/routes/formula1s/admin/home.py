# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from formula1_app import facade
from routes.formula1s.admin import new, edit


def delete(_handler, formula1_id):
    facade.delete_formula1_cmd(formula1_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_formula1s_cmd()
    formula1s = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.formula1_short_form()

    def short_formula1_dict(formula1):
        formula1_dct = short_form.fill_with_model(formula1)
        formula1_dct['edit_path'] = router.to_path(edit_path, formula1_dct['id'])
        formula1_dct['delete_path'] = router.to_path(delete_path, formula1_dct['id'])
        return formula1_dct

    short_formula1s = [short_formula1_dict(formula1) for formula1 in formula1s]
    context = {'formula1s': short_formula1s,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

