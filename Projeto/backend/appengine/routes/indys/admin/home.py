# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from indy_app import facade
from routes.indys.admin import new, edit


def delete(_handler, indy_id):
    facade.delete_indy_cmd(indy_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_indys_cmd()
    indys = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.indy_short_form()

    def short_indy_dict(indy):
        indy_dct = short_form.fill_with_model(indy)
        indy_dct['edit_path'] = router.to_path(edit_path, indy_dct['id'])
        indy_dct['delete_path'] = router.to_path(delete_path, indy_dct['id'])
        return indy_dct

    short_indys = [short_indy_dict(indy) for indy in indys]
    context = {'indys': short_indys,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

