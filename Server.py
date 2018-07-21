import os

import cv2
import face_recognition

import Database
from FaceCapture import FaceCapture
from MachineLearning import MachineLearning
from MonitorPool import MonitorPool


class Backend:
    def __init__(self):
        self.is_running = True
        self.monitor_pool = MonitorPool()
        self.delay = 0.1
        self.database = Database.Database()
        self.known_face_encodings = []
        self.students_id = []
        self.machine_learning = MachineLearning()
        self.face_capture = FaceCapture(self.database, self.machine_learning)

    def read_config(self):
        for e in self.database.monitor_readAll():
            self.monitor_pool.addMonitor(e)

    def read_images(self):
        path = 'image'
        person_list = os.listdir(path)  # 列出文件夹下所有的目录与文件
        for i, person_id in enumerate(person_list):
            person_img_path = os.path.join(path, person_id)
            for i2, pics in enumerate(os.listdir(person_img_path)):
                img_path = os.path.join(person_img_path, pics)
                if os.path.isfile(img_path):
                    encodings = self.machine_learning.face_encoding(img_path)
                    if encodings:
                        encoding = encodings[0]

                        self.known_face_encodings.append(encoding)
                        self.students_id.append(person_id)
                    else:
                        os.remove(img_path)

    def open_capture(self):

        video_capture = cv2.VideoCapture(0)

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)

                if True in matches:
                    first_match_index = matches.index(True)
                    name = str(self.students_id[first_match_index])
                else:
                    name = "Unknown"

                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

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
    backend.read_images()
    backend.open_capture()
