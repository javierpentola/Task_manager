import sqlite3

def init_db():
    conn = sqlite3.connect('restaurant_tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT, shift TEXT, assigned_to TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
