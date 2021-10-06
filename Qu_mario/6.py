import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #창 크기 고정
        self.setFixedSize(240, 224)
        #창 제목 설정
        self.setWindowTitle('GA-mario')

        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        env.reset()

        screen = env.get_screen()

        #이미지
        label_image = QLabel(self)
        qimage = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        self.setFixedSize(480, 448)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)

        #창 띄우기
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())