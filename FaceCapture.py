import os
import random

import cv2
import face_recognition
import numpy as np

from Database import Database
from Student import Student


class FaceCapture:
    def __init__(self, database, machine_learning, students):
        self.students = students
        self.machine_learning = machine_learning
        self.database = database
        self.img_root_path = 'image'
        self.encoding_root_path = 'encoding'

    def gamma_trans(self, img, gamma):  # gamma函数处理
        gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
        gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
        return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。

    def save_file(self, face_image, student):

        # img_path = os.path.join(self.img_root_path, str(student.get_id()))
        #
        # if not os.path.exists(img_path):
        #     os.mkdir(img_path)

        encoding_path = os.path.join(self.encoding_root_path, str(student.get_id()))
        if not os.path.exists(encoding_path):
            os.mkdir(encoding_path)

        person_list = os.listdir(encoding_path)  # 列出文件夹下所有的目录与文件
        if random.randint(0, len(person_list) * len(person_list)) > 50:
            return
        for gamma_int in range(5, 16, 5):
            gamma = gamma_int / 10

            image_gamma_correct = self.gamma_trans(face_image, gamma)  # 2.5为gamma函数的指数值，大于1曝光度下降，大于0小于1曝光度增强
            encodings = face_recognition.face_encodings(image_gamma_correct)

            if encodings:
                encoding = encodings[0]
                random_int = random.randint(0, 40)
                # img_file = os.path.join(img_path, "{}_{}.jpg".format(random_int, gamma))
                encoding_file = os.path.join(encoding_path, "{}_{}.npz".format(random_int, gamma))

                student.encodings.append(encoding)

                # cv2.imwrite(img_file, image_gamma_correct)
                np.save(encoding_file, encoding)
                print("saved", encoding_file)

    def read_img(self, img, frame_num):
        # cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
        faces = self.machine_learning.face_split(img)
        for e_face in faces:
            encodings = face_recognition.face_encodings(e_face)
            if encodings:
                encoding = encodings[0]
                rst = self.machine_learning.face_compare(self.students, encoding)
                if not rst:
                    stu = Student(None, "Unkonwn", "", "", "", "", "")
                    self.database.student_entry(stu)
                    stu.set_id(self.database.student_max_ID())
                    self.students.append(stu)

                else:
                    stu = rst

                self.save_file(img, stu)


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
