import database

def InsertVote(name, id):
    cur = database.cursor
    con = database.koneksi

    value = (name, id)
    cur.execute("INSERT INTO vote (name, id_pendaftar) VALUES(?, ?);", value)
    con.commit()

def CountVote():
  cur = database.cursor
  con = database.koneksi

  data = []

  cur.execute("select *, (select count(id) from vote where id_pendaftar = pendaftar.id) as count from pendaftar")
  for row in cur.fetchall():
    object = {"Id": row[0], "Name": row[1], "Count": row[2]}
    data.append(object)
  con.commit()

  return data