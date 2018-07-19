from Tools import NotCompleted


class MonitorSession:
    def __init__(self):
        self.addr = None
        self.connect_addr = None

    def setAddr(self, addr):
        self.addr = addr

    def connect(self, connect_addr):
        self.connect_addr = connect_addr
        # todo
        raise NotCompleted()

    def section(self):
        """
            This method shall be used to fetch a pic from a current monitor stream
        :return:
        """
        raise NotCompleted()

