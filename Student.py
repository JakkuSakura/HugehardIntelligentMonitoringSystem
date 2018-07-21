class Student:
    def __init__(self, id, name, gender, birthday, student_id, grade, clas):
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

    def __str__(self):
        return "Student({}, {}, {}, {})".format(self.id, self.name, self.grade, self.clas)

