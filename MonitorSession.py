import cv2

from Tools import NotCompleted, CamConnectError


class MonitorSession:
    def __init__(self):
        self.connect_addr = None
        self.cap = None

    def setAddr(self, addr):
        """

        :param addr: for instance:  rtsp://192.168.1.60/stream2
        :return:
        """
        self.connect_addr = addr

    def connect(self):
        if self.connect_addr.startwith("rtmp://"):
            self.cap = cv2.VideoCapture()
            self.cap.open(self.connect_addr)
        else:
            self.cap = cv2.VideoCapture(self.connect_addr)

        if not self.cap.isOpened():
            raise CamConnectError()

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


if __name__ == '__main__':
    session1 = MonitorSession()
    session1.setAddr("rtsp://cloud.easydarwin.org:554/606034.sdp")
    session1.connect()
    frame = session1.section()
    cv2.namedWindow("Image")
    cv2.imshow("Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    session1.clean()
