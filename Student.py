from Monitor import Monitor


class Student:
    def __init__(self, id=None, name="", gender="", birthday="", student_id="", grade="", clas=""):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.student_id = student_id
        self.grade = grade
        self.clas = clas
        self.monitor_zone: Monitor = None
        self.encodings = []

    def set_zone(self, monitor):
        self.monitor_zone = monitor

    def get_zone(self):
        return self.monitor_zone

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

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

    def to_list(self):
        lst = [self.id, self.name, self.gender, self.birthday, self.student_id, self.grade,
               self.clas]
        if self.monitor_zone:
            return lst + self.monitor_zone.to_list()
        else:
            return lst

    def __str__(self):
        return "Student({}, {}, {}, {})".format(self.id, self.name, self.grade, self.clas)
