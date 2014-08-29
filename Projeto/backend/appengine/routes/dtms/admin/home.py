# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from dtm_app import facade
from routes.dtms.admin import new, edit


def delete(_handler, dtm_id):
    facade.delete_dtm_cmd(dtm_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_dtms_cmd()
    dtms = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.dtm_short_form()

    def short_dtm_dict(dtm):
        dtm_dct = short_form.fill_with_model(dtm)
        dtm_dct['edit_path'] = router.to_path(edit_path, dtm_dct['id'])
        dtm_dct['delete_path'] = router.to_path(delete_path, dtm_dct['id'])
        return dtm_dct

    short_dtms = [short_dtm_dict(dtm) for dtm in dtms]
    context = {'dtms': short_dtms,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

