import sqlite3
class Student:
    def __init__(self,id, name, gender, birthday, student_id, grade, clas):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.student_id = student_id
        self.grade = grade
        self.clas = clas

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_birthday(self):
        return self.birthday

    def get_student_id(self):
        return self.student_id

    def get_grade(self):
        return self.grade

    def get_clas(self):
        return self.clas


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()

    def create_studentsDB(self):
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS Students
                (
                    id integer PRIMARY KEY, 
                    name varchar(20),
                    gender varchar(2),
                    birthday date,
                    student_id varchar(20),
                    grade varchar(10),
                    class varchar(10)
                )
            """)
        self.conn.commit()
    '''
    def execute(self, sql):
        result = self.cur.execute(*sql)
        self.conn.commit()
        return result

    def query(self, sql):
        return self.cur.execute(*sql)
    '''
    def clean(self):
        self.cur.close()
        self.conn.close()

    def student_entry(self, student):
        self.cur.execute("""INSERT INTO Students VALUES (?,?,?,?,?,?,?)""",(student.id,student.name,student.gender,student.birthday,student.student_id,student.grade,student.clas))
        self.conn.commit()

    def student_read_byID(self, id):
        self.cur.execute('SELECT * FROM Students WHERE id = ?', (id,))
        for row in self.cur.fetchall():
            print(row)
        self.conn.commit()

    def student_readAll(self):
        self.cur.execute('SELECT * FROM Students')
        for row in self.cur.fetchall():
            print(row)
        self.conn.commit()

    def student_remove(self, id):
        self.cur.execute('DELETE FROM Students WHERE id = ?',(id,))
        self.conn.commit()


root = Database()
'''
if __name__ == '__main__':
    root.execute((
        r"""
            CREATE TABLE IF NOT EXISTS students
            (
                id integer, 
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
'''
root.create_studentsDB()
#root.student_remove(1)
student1 = Student(1,'a','aa',2018,1,1,1)
#root.student_entry(student1)
root.student_read_byID(2)
#root.student_readAll()
root.clean()
