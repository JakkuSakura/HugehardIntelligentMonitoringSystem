import cv2

from Tools import CamConnectError


class Monitor:
    def __init__(self, id=None, addr=None, physical_location=None, type=None):
        self.id = id
        self.addr = addr
        self.physical_location = physical_location
        self.type = type
        self.popu = 0
        self.cap = None

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

    def set_addr(self, addr):
        """
        :param addr: for instance:  rtsp://192.168.1.60/stream2
        :return:
        """
        self.addr = addr

    def connect(self):
        # if self.addr.startswith("rtmp://"):
        #     self.cap = cv2.VideoCapture()
        #     self.cap.open(self.addr)
        # else:
        self.cap = cv2.VideoCapture(self.addr)

        if not self.cap.isOpened():
            raise CamConnectError()

    def set_popu(self, p):
        self.popu = p

    def get_popu(self):
        return self.popu

    def section(self):
        """
            This method shall be used to fetch a pic from a current monitor stream
        :return:
        """

        if self.cap.isOpened():
            flag, frame = self.cap.read()

            return frame
        else:
            raise CamConnectError()

    def clean(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def to_list(self):
        return [self.id, self.addr, self.physical_location, self.type, self.popu]


if __name__ == '__main__':
    session1 = Monitor()
    session1.set_addr(0)
    session1.connect()
    frame = session1.section()
    cv2.namedWindow("Image")
    cv2.imshow("Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    session1.clean()
