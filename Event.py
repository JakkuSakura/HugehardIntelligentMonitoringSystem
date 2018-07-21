import sqlite3

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

    def set_monitor_id(self, get_monitor_id):
        self.get_monitor_id = get_monitor_id

    def search_id(self,id_0):
        import sqlite3
        conn = sqlite3.connect('test.db')
        c = conn.execute()
        print ("Opened database successfully")
        cursor = c.execute("SELECT id, appeartime, monitor_id  from event")
        for row in cursor:
            if(id == id_0):
                print("ID = ", id_0)
                print("At ", row[1])
                print("The person was in the monitoring of", row[2], "\n")
        conn.close()

    def __str__(self):
        return "Event({}, {}, {}, {})".format(self.id, self.student_id, self.appeartime, self.monitor_id)
