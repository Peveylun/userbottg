import sqlite3


class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS some_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        data TEXT NOT NULL)""")

    def create(self, text) -> None:
        self.cur.execute(f"""INSERT INTO some_table (data) VALUES ('{text}')""")
        self.conn.commit()

    def get(self) -> str:
        temp = self.cur.execute("""SELECT * FROM some_table""").fetchall()
        str = ''
        count = 0
        for i in range(len(temp)):
            count += 1
            str += f"{count} | {temp[i][1]}\n"
        return str

    def delete(self, text) -> None:
        self.cur.execute(f"""DELETE FROM some_table WHERE data='{text}'""")
        self.conn.commit()
