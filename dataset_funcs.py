import sqlite3

def create_table():
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS amount (code TEXT PRIMARY KEY)')
    c.execute('ALTER TABLE amount ADD COLUMN name TEXT')
    conn.commit()
    conn.close()
    conn.close()

def create_share(name, code):
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('INSERT INTO amount (name, code) VALUES ("{}", "{}")'.format(name, code))
    conn.commit()
    conn.close()

def add_column(date):
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('ALTER TABLE amount ADD COLUMN "{}" INTERAGE'.format(date))
    conn.commit()
    conn.close()

def update_data(name, date, data):
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute("""
        UPDATE amount
        SET "{}" = {}
        WHERE code = '{}'
        """.format(date, data, name))
    conn.commit()
    conn.close()
    
def get_data():
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('SELECT * FROM amount')
    return c.fetchall()

def get_column():
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('PRAGMA table_info(amount)')
    return [i[1] for i in c.fetchall()][2:]

def get_share_90(name):
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('SELECT * FROM amount WHERE name = "{}"'.format(name))
    share_data = c.fetchall()
    conn.close()
    return share_data[0][:2], share_data[0][-90:]

def get_share(name):
    conn = sqlite3.connect('shares.db')
    c = conn.cursor()
    c.execute('SELECT * FROM amount WHERE name = "{}"'.format(name))
    share_data = c.fetchall()
    conn.close()
    return share_data[0][:2], share_data[0][2:]
