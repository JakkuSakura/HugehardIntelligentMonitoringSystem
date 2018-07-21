import os
import random

import Database
import face_recognition
import cv2


# Load a sample picture and learn how to recognize it.
known_face_encodings = []

known_face_names = []

path = 'image'
list = os.listdir(path)  # 列出文件夹下所有的目录与文件
for i, person_id in enumerate(list):
    person_img_path = os.path.join(path, person_id)
    for i2, pics in enumerate(os.listdir(person_img_path)):
        e2_path = os.path.join(person_img_path, pics)
        if os.path.isfile(e2_path):
            result = Database.root.query((r"SELECT * FROM `students` WHERE `id`=?", (person_id,)))
            image = face_recognition.load_image_file(e2_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)

            known_face_names.append(result.fetchall()[0][1])


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
# Create arrays of known face encodings and their names

# Initialize some variables
face_locations = []
face_encodings = []
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
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

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
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        id = input("person id here")
        cv2.imwrite(os.path.join(path, id, "%d.jpg" % random.randint(0, 100)), frame)


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()