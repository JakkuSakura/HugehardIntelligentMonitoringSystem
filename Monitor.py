
class Monitor:
    def __init__(self, id, addr, physical_location, type):
        self.id = id
        self.addr = addr
        self.physical_location = physical_location
        self.type = type

    def get_id(self):
        return self.id

    def get_addr(self):
        return self.addr

    def get_physical_location(self):
        return self.physical_location

    def get_type(self):
        return self.type

    def __str__(self):
        return "Monitor({}, {}, {}, {})".format(self.id, self.addr, self.physical_location, self.type)
