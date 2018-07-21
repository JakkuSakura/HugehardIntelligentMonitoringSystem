import copy
import os

import cv2
import face_recognition

import Database
from MonitorPool import MonitorPool
from Tools import NotCompleted


class Backend:
    def __init__(self):
        self.is_running = True
        self.monitor_entrance = MonitorPool()
        self.monitor_pool = MonitorPool()
        self.delay = 0.1
        self.database = Database.Database()
        self.known_face_encodings = []
        self.known_face_names = []

    def read_config(self):
        for e in self.database.monitor_readAll():
            if e.get_type() == 'entrance':
                self.monitor_entrance.addMonitor(e)
            else:
                self.monitor_pool.addMonitor(e)

    def read_images(self):
        path = 'image'
        list = os.listdir(path)  # 列出文件夹下所有的目录与文件
        for i, person_id in enumerate(list):
            person_img_path = os.path.join(path, person_id)
            for i2, pics in enumerate(os.listdir(person_img_path)):
                e2_path = os.path.join(person_img_path, pics)
                if os.path.isfile(e2_path):
                    image = face_recognition.load_image_file(e2_path)
                    encoding = face_recognition.face_encodings(image)[0]
                    self.known_face_encodings.append(encoding)

                    student = self.database.student_read_byID(person_id)
                    if student:
                        self.known_face_names.append(student.get_name())
                    else:
                        self.known_face_names.append("DP " + str(person_id))

    def open_capture(self):

        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)
        # Create arrays of known face encodings and their names

        # Initialize some variables
        face_locations = []
        face_names = []
        process_this_frame = True
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_face_names[first_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
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
        while self.is_running:
            for e in self.monitor_entrance.getMonitors():
                frame = e.section()
                encodings = face_recognition.face_encodings(frame)
                if len(encodings):
                    raise NotCompleted()
            for e in self.monitor_pool.getMonitors():
                frame = e.section()
                encodings = face_recognition.face_encodings(frame)
                for e_encoding in encodings:
                    raise NotCompleted()


if __name__ == '__main__':
    backend = Backend()
    backend.read_images()
    backend.open_capture()
