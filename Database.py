import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()

    def execute(self, sql):
        result = self.cur.execute(*sql)
        self.conn.commit()
        return result

    def query(self, sql):
        return self.cur.execute(*sql)

    def clean(self):
        self.cur.close()
        self.conn.close()


root = Database()

if __name__ == '__main__':
    root.execute((
        r"""
            CREATE TABLE students
            (
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar(20),
                gender varchar(2),
                birthday date,
                student_id varchar(20),
                grade varchar(10),
                class varchar(10)
            );
        """,))

    root.execute((
        r"""
            CREATE UNIQUE INDEX students_id_uindex ON `students` (id);
        """,))

    root.clean()
