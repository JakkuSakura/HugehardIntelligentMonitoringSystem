import os
import random
import threading

import cv2
import face_recognition

from Database import Database
from Student import Student


class FaceCapture:
    def __init__(self, database, machine_learning, saved_encoding, saved_id):
        self.saved_persons_encoding = saved_encoding
        self.saved_persons_id = saved_id
        self.machine_learning = machine_learning
        self.database = database
        self.path = 'image'

    def read_img(self, img, frame_num):
        faces = self.machine_learning.face_split(img)
        for e_face in faces:
            encodings = face_recognition.face_encodings(e_face)
            if encodings:
                encoding = encodings[0]

                rst = self.machine_learning.face_compare(self.saved_persons_encoding, encoding)
                if rst == -1:
                    stu = Student(None, "Unkonwn", "", "", "", "", "")
                    self.database.student_entry(stu)
                    stu.set_id(self.database.student_max_ID())

                    self.saved_persons_encoding.append(encoding)
                    self.saved_persons_id.append(stu.get_id())

                else:
                    stu = self.database.student_read_byID(self.saved_persons_id[rst])
                path = os.path.join(self.path, str(stu.get_id()))
                if not os.path.exists(path):
                    os.mkdir(path)
                file = os.path.join(path, "{}.jpg".format(random.randint(0, 20)))
                cv2.imwrite(file, e_face)

                print("saved", file)


if __name__ == '__main__':
    Database().student_clearAll()
    # session1 = Monitor()
    # session1.setAddr(0)
    # session1.connect()
    # fc = FaceCapture(Database(), MachineLearning(),[], [])
    # for i in range(10000):
    #     frame = session1.section()
    #     fc.read_img(frame, i)
    # session1.clean()
