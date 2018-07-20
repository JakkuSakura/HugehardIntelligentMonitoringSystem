import face_recognition


class MachineLearning:
    def __init__(self):
        pass

    def face_location(self, img_file_addr):
        image = face_recognition.load_image_file(img_file_addr)
        face_locations = face_recognition.face_locations(image, model="cnn")
        return face_locations

    def face_encoding(self, img_file_addr):
        image = face_recognition.load_image_file(img_file_addr)
        face_encodings = face_recognition.face_encodings(image)
        return face_encodings

    def face_compare(self, face_encoding_list, face_encoding):
        results = face_recognition.compare_faces(face_encoding_list, face_encoding)
        for i, e in enumerate(results):
            if e:
                return i
        else:
            return -1


if __name__ == '__main__':
    ml = MachineLearning()
    print(ml.face_location("image/4.jpg"))
