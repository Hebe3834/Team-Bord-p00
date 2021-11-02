import sqlite3   #enable control of an sqlite database

DB_FILE="users.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

command = '''CREATE TABLE IF NOT EXISTS logins(
    username TEXT NOT NULL PRIMARY KEY UNIQUE, 
    password TEXT NOT NULL)'''
c.execute(command)
