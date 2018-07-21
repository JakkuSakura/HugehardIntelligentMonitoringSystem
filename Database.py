import sqlite3

from Monitor import Monitor
from Student import Student


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()

    def create_monitorsDB(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS monitors 
                            (
                                id integer PRIMARY KEY AUTOINCREMENT, 
                                addr text, 
                                physical_location text,
                                type text
                            )
                        """)
        self.conn.commit()

    def monitor_entry(self, monitor):
        self.cur.execute("""INSERT INTO monitors VALUES (?,?,?,?)""", (
            monitor.id, monitor.addr, monitor.physical_location, monitor.type))
        self.conn.commit()

    def monitor_read_byID(self, id):
        rst = self.cur.execute('SELECT * FROM monitors WHERE id = ?', (id,))
        return rst.fetchall()[0]

    def monitor_readAll(self):
        self.cur.execute('SELECT * FROM monitors')
        monitors = self.cur.fetchall()
        r_monitors = []
        for e in monitors:
            r_monitors.append(Monitor(*e))
        return r_monitors

    def monitor_remove_byID(self, id):
        self.cur.execute('DELETE FROM monitors WHERE id = ?', (id,))
        self.conn.commit()

    def monitor_clearAll(self):
        self.cur.execute('DELETE FROM monitors')
        self.conn.commit()

    def create_studentsDB(self):
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS Students
                (
                    id integer PRIMARY KEY AUTOINCREMENT, 
                    name varchar(20),
                    gender varchar(2),
                    birthday date,
                    student_id varchar(20),
                    grade varchar(10),
                    class varchar(10)
                )
            """)
        self.conn.commit()

    def execute(self, sql):
        result = self.cur.execute(*sql)
        self.conn.commit()
        return result

    def query(self, sql):
        return self.cur.execute(*sql)

    def clean(self):
        self.cur.close()
        self.conn.close()

    def student_entry(self, student):
        self.cur.execute("""INSERT INTO Students VALUES (?,?,?,?,?,?,?)""", (
            student.id, student.name, student.gender, student.birthday, student.student_id, student.grade,
            student.clas))
        self.conn.commit()

    def student_read_byID(self, id):
        stu = self.cur.execute('SELECT * FROM Students WHERE id = ?', (id,)).fetchone()
        if stu:
            return Student(*stu)
        else:
            return None

    def student_readAll(self):
        rst = self.cur.execute('SELECT * FROM Students')
        r_students = []
        for e in rst:
            r_students.append(Student(*e))
        return r_students

    def student_remove_byID(self, id):
        self.cur.execute('DELETE FROM Students WHERE id = ?', (id,))
        self.conn.commit()

    def student_clearAll(self):
        self.cur.execute('DELETE FROM Students')
        self.conn.commit()



if __name__ == '__main__':
    root = Database()
    root.create_studentsDB()
    root.student_remove_byID(1)
    root.student_clearAll()
    student1 = Student(2, 'Jack', 'M', "2018.1.1", "37072333", "Grade 1", "Class 1")
    root.student_entry(student1)
    print(root.student_read_byID(2))
    all = root.student_readAll()
    for e in all:
        print(e, end=", ")
    print()

    root.create_monitorsDB()

    root.monitor_clearAll()

    monitor1 = Monitor(1, 'rtsp://127.0.0.1/', 'weifang', 'entrance')
    root.monitor_entry(monitor1)
    for e in root.monitor_readAll():
        print(e)
    root.clean()
