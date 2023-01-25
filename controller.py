from model import *
from pycnic.core import Handler

class AddPendaftar(Handler):
  def post(self):
    name = self.request.data["name"]

    InsertData(name)
    return {'message': 'Success'}

class ListPendaftar(Handler):
  def get(self):

    data = ListData()
    return data
  
class EditPendaftar(Handler):
  def post(self):
    id = self.request.data["id"]

    data = EditData(id)
    return data
  
class UpdatePendaftar(Handler):
  def post(self):
    id = self.request.data["id"]
    name = self.request.data["name"]

    UpdateData(id, name)
    return {'message': 'Success'}

class DeletePendaftar(Handler):
  def post(self):
    id = self.request.data["id"]

    DeleteData(id)
    return {'message': 'Success'}