import cv2

class Camera():
    def __init__(self):
        self.cam = None
        self.current_frame = None
        self.detected_codes = []
        self.detected_objects = []

    def set_camera(self, file):
        self.cam = cv2.VideoCapture(file)

    def read_frame(self):
        ret, frame = self.cam.read()
        if not ret:
            print("failed to grab frame")
            return
        cv2.imshow("source", frame)

    def detect_barcode(self):
        # TODO:
        # detect barcodes in current_frame
        # append results to detected_codes list
        pass

    def detect_object(self):
        # TODO:
        # detect fruit, vegetables and bottles in current_frame
        # if detected object is bottle do detect_text() on bottle
        # append results to detected_objects list
        pass

    def detect_text(self, img):
        # TODO:
        # detect text in img
        # map results to valid classifier
        # return classifier
        pass