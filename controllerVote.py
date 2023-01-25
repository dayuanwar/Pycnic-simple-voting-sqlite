from modelVote import *
from pycnic.core import Handler

class SaveVote(Handler):
  def post(self):
    name = self.request.data["name"]
    id = self.request.data["id"]

    InsertVote(name, id)
    return {'message': 'Success'}

class ListCount(Handler):
  def get(self):

    data = CountVote()
    return data