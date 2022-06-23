import sqlite3

__connection = None

def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('d.db', check_same_thread=False)
    return __connection


def init_db(force: bool = False):
    conn = get_connection()

    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS lists')

    c.execute('''
                CREATE TABLE IF NOT EXISTS lists(
                id INTEGER PRIMARY KEY,
                text TEXT NOT NULL,
                ok BOOLEAN NOT NULL
            )
    ''')
    conn.commit()


def dellAll():
    init_db(True)


def addTask(text: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO lists (text, ok) VALUES (?,?)", (text, False,))
    conn.commit()


def delTask(id: int):
    conn = get_connection()
    conn.execute('''DELETE FROM lists WHERE id=?''', (id,))
    conn.commit()


def getTasks():
    conn = get_connection()
    c = conn.execute("SELECT id, text, ok from lists ORDER BY id ASC ")
    text = []
    for row in c:
        text.append(row)
    return text

def editTaskOk(id: int):
    conn = get_connection()
    c = conn.execute("SELECT ok from lists WHERE id = (?)", (id,))
    c.execute('''UPDATE lists SET ok=? WHERE id=?''', (not bool(c.fetchone()[0]), id))
    conn.commit()


if __name__ == '__main__':
    init_db(force = False)