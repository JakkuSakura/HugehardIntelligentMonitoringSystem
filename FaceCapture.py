import os
import random

import cv2

from MachineLearning import MachineLearning
from MonitorSession import MonitorSession
from Student import Student


class FaceCapture:
    def __init__(self, database):
        self.saved_persons = []
        self.saved_persons_id = []
        self.machine_learning = MachineLearning()
        self.database = database
        self.path = 'image'

    def read_img(self, img, frame_num):
        if frame_num % 10 != 0:
            return
        faces = self.machine_learning.face_split(img)
        for e_face in faces:
            rst = self.machine_learning.face_compare(self.saved_persons, e_face)
            if rst == -1:
                stu = Student(None, "Unkonwn", "", "", "", "", "")
                self.database.student_entry(stu)
                stu.set_id(self.database.student_max_id())

                self.saved_persons.append(e_face)
                self.saved_persons_id.append(stu.get_id())
            else:
                stu = self.database.student_read_byID(self.saved_persons_id[rst])

            cv2.imwrite(os.path.join(self.path, stu.get_id(), "{}.jpg".format(random.randint(0, 20))), e_face)


if __name__ == '__main__':
    pass