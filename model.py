import database
from pycnic.core import Handler

def InsertData(name):
    cur = database.cursor
    con = database.koneksi

    value = (name,)
    cur.execute("INSERT INTO pendaftar (name) VALUES(?);", value)
    con.commit()

def ListData():
  cur = database.cursor
  con = database.koneksi

  data = []

  cur.execute("SELECT * FROM pendaftar")
  for row in cur.fetchall():
    object = {"Id": row[0], "Name": row[1]}
    data.append(object)
  con.commit()

  return data

def EditData(id):
  cur = database.cursor
  con = database.koneksi

  converted = "% s" % id
    
  cur.execute("SELECT * FROM pendaftar WHERE id = '"+converted+"'")
  for row in cur.fetchall():
    object = {"Id": row[0], "Name": row[1]}
  con.commit()

  return object

def UpdateData(id, name):
    cur = database.cursor
    con = database.koneksi
    converted = "% s" % id

    cur.execute("UPDATE pendaftar SET name = '"+name+"' WHERE id = '"+converted+"'")
    con.commit()

def DeleteData(id):
    cur = database.cursor
    con = database.koneksi
    converted = "% s" % id

    cur.execute("DELETE FROM pendaftar WHERE id = '"+converted+"'")
    con.commit()