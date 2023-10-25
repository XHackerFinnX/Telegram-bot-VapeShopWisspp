import sqlite3 as sq

with sq.connect("db\\database.db") as con:
    cur = con.cursor()
    
    
    cur.execute('''CREATE TABLE IF NOT EXISTS name_single (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER,
        count INTEGER,
        number_id INTEGER
    )
    ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS name_liquid (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER,
        count INTEGER,
        number_id INTEGER
    )
    ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS name_stock_all (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER,
        count INTEGER,
        number_id INTEGER
    )
    ''')

def sql_name_single(next_id):
    with sq.connect("db\\database.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT name, price FROM name_single WHERE number_id = {next_id}")
        result_single = cur.fetchall()
        return result_single[0][0], result_single[0][1]

def sql_name_liquid(next_id):
    with sq.connect("db\\database.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT name, price FROM name_liquid WHERE number_id = {next_id}")
        result_liquid = cur.fetchall()
        return result_liquid[0][0], result_liquid[0][1]

def sql_name_stock_all(next_id):
    with sq.connect("db\\database.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT name, price FROM name_stock_all WHERE number_id = {next_id}")
        result_stock = cur.fetchall()
        return result_stock[0][0], result_stock[0][1]
    






