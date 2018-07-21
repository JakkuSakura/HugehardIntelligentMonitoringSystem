class Event:
    def __init__(self, id, student_id, appeartime, monitor_id):
        self.id = id
        self.student_id = student_id
        self.appeartime = appeartime
        self.monitor_id = monitor_id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_appeartime(self):
        return self.appeartime

    def set_appeartime(self, appeartime):
        self.appeartime = appeartime

    def get_monitor_id(self):
        return self.monitor_id

    def get_monitor_id(self, get_monitor_id):
        self.get_monitor_id = get_monitor_id

    def __str__(self):
        return "Event({}, {}, {}, {})".format(self.id, self.student_id, self.appeartime, self.monitor_id)
