# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class ClassificacaoPilotos(Node):
    pilotos = ndb.StringProperty(required=True)
    equipe = ndb.StringProperty(required=True)
    categoria = ndb.StringProperty(required=True)
    pontos = ndb.IntegerProperty(required=True)
    texto = ndb.StringProperty(required=True)

