
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from UI.screenSampleWindow import Ui_Form_screenSampleWindow

from screen import ScreenDraw, ScreenGet
from image_processing.Qt2CV import QPixmap2OpenCVImage

import time


class ScreenSampleWindow(QWidget):

    def __init__(self):
        super(ScreenSampleWindow, self).__init__()

        # mouse tracking
        self.setMouseTracking(True)
        self.mouse_button_pressed = False
        self.last_mouse_track_time = 0

        # connect window ui and Widget
        self.window_ui = Ui_Form_screenSampleWindow()
        self.window_ui.setupUi(self)
        self.window_ui.retranslateUi(self)

        # draw screen
        self.screen = ScreenDraw()
        self.screen.setPenColor(255, 0, 0)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)

        # screen shot
        self.screenShot = ScreenGet()
        self.screenShot.start()

        self.show()

    def draw_rect(self):
        result = self.geometry()
        x, y, w, h = result.x(), result.y(), result.width(), result.height()

        self.screen.drawRect(x, y, w, h)

    def get_window_image(self):
        result = self.geometry()
        x, y, w, h = result.x(), result.y(), result.width(), result.height()
        pixmap = self.screenShot.getScreen(x, y, w, h)
        image = pixmap.toImage()
        return QPixmap2OpenCVImage(image)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if not self.mouse_button_pressed:
                self.mouse_button_pressed = True
                self.dx = event.globalX() - self.x()
                self.dy = event.globalY() - self.y()
                event.accept()
            else:
                if self.mouse_button_pressed:
                    self.mouse_button_pressed = False
                    event.accept()

    def mouseMoveEvent(self, event):
        # mouse move tracking don't need too fast, otherwise it will crash
        current_time = time.time()
        if current_time < self.last_mouse_track_time + 0.1:
            return None
        self.last_mouse_track_time = current_time

        if self.mouse_button_pressed:
            x = event.globalX()
            y = event.globalY()
            self.move(x - self.dx, y - self.dy)



