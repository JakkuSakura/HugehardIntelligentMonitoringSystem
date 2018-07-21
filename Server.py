import os

import cv2
import face_recognition
import numpy

import Database
from FaceCapture import FaceCapture
from MachineLearning import MachineLearning
from MonitorPool import MonitorPool
from Student import Student


class Backend:
    def __init__(self):
        self.is_running = True
        self.monitor_pool = MonitorPool()
        self.tolerance = 0.3
        self.database = Database.Database()
        self.students = []
        self.machine_learning = MachineLearning()
        self.face_capture = FaceCapture(self.database, self.machine_learning, self.students)

    def read_config(self):
        for e in self.database.monitor_readAll():
            self.monitor_pool.addMonitor(e)

    def read_encodings(self):

        path = 'encoding'
        person_list = os.listdir(path)  # 列出文件夹下所有的目录与文件
        for i, person_id in enumerate(person_list):
            person_encoding_path = os.path.join(path, person_id)
            stu = Student()
            self.students.append(stu)
            stu.set_id(person_id)
            for i2, pics in enumerate(os.listdir(person_encoding_path)):
                encoding_path = os.path.join(person_encoding_path, pics)
                if os.path.isfile(encoding_path):
                    encoding = numpy.load(encoding_path)
                    stu.encodings.append(encoding)

    def open_capture(self):

        video_capture = cv2.VideoCapture(0)
        cv2.namedWindow("Video")
        frame_num = 0
        face_locations = []
        face_names = []
        while True:
            ret, frame = video_capture.read()
            print(ret, frame)
            if frame_num % 7 == 0:
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                self.face_capture.read_img(frame, frame_num)

                face_names = []

                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    rst = self.machine_learning.face_compare(self.students, face_encoding)
                    if rst:
                        face_names.append(rst.get_id())

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)
            frame_num += 1

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    def run(self):
        frame_num = 0
        while self.is_running:
            for e in self.monitor_pool.getMonitors():
                frame = e.section()
                self.face_capture.read_img(frame, frame_num)

            frame_num += 1


if __name__ == '__main__':
    backend = Backend()
    backend.read_encodings()
    backend.open_capture()
