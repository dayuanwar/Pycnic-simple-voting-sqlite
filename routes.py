from controller import *
from controllerVote import *
from pycnic.core import WSGI

class app(WSGI):
  headers = [("Access-Control-Allow-Origin", "*")]
  routes = [
            ('/add', AddPendaftar()),
            ('/list', ListPendaftar()),
            ('/edit', EditPendaftar()),
            ('/update', UpdatePendaftar()),
            ('/delete', DeletePendaftar()),
            ('/vote', SaveVote()),
            ('/count-vote', ListCount()),
  ]