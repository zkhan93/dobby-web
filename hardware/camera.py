from picamera.array import PiRGBArray
from picamera import PiCamera
import os
from datetime import datetime
import cv2


class Camera(object):
    img = None

    def open_eyes(self, base_path='.'):
        self.eye_path = os.path.join(base_path, 'eyes')
        self.imgCount = 0
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(1280, 720))
        self.imageStream = self.camera.capture_continuous(self.rawCapture,
                                                          format="bgr",
                                                          use_video_port=True)

    def close_eyes(self):
        try:
            if self.camera:
                self.camera.close()
        except Exception as ex:
            print 'Error closing eyes', str(ex)

    def get_frame(self, save=False):
        img = next(self.imageStream)
        if img is not None:
            self.img = img.array
        if save:
            self._saveFrame(self.img)
        self.rawCapture.truncate(0)
        return self.img

    def _saveFrame(self, img):
        folder = os.path.join(self.eye_path, 'img')
        if img is not None:
            filename = 'IMG_%s.jpg' % datetime.today().strftime('%Y%m%d%H%I%S')
            if not os.path.exists(folder):
                os.mkdir(folder)
            path = os.path.join(folder, filename)
            cv2.imwrite(path, img)
