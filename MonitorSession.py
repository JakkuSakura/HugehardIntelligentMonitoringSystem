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
        self.cap = cv2.VideoCapture(self.connect_addr)
        if not self.cap.isOpened():
            raise CamConnectError()

    def section(self):
        """
            This method shall be used to fetch a pic from a current monitor stream
        :return:
        """

        frame_num = 1

        while self.cap.isOpened():

            ret, frame = self.cap.read()

            print(frame_num)

            frame_num = frame_num + 1

            cv2.imshow('frame', frame)

            # 每10帧存储一张图片

            if frame_num % 10 == 1:
                cv2.imwrite('image' + str(frame_num) + '.jpg', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        raise NotCompleted()

    def clean(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    session = MonitorSession()
    session.setAddr("rtmp://live.hkstv.hk.lxdns.com/live/hks")
    session.connect()
    session.section()
    session.clean()
