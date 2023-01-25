import sqlite3

koneksi = sqlite3.connect('voting.db')
cursor = koneksi.cursor()

pendaftar = '''CREATE TABLE IF NOT EXISTS pendaftar (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL);'''
vote = '''CREATE TABLE IF NOT EXISTS vote (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, id_pendaftar INTEGER);'''

cursor.execute(pendaftar)
cursor.execute(vote)
koneksi.commit()