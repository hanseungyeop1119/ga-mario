import retro
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, \
    QWidget, QLabel, QPushButton

import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #창 크기 고정
        self.setFixedSize(480, 448)
        #창 제목 설정
        self.setWindowTitle('GA-mario')

        self.press_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 이미지
        self.label_image = QLabel(self)

        # 게임 환경 생성
        self.env = retro.make(game='SuperMarioBros-Nes', state='Level8-1')
        # 새 게임 시작
        self.env.reset()
        # 화면 가져오기
        self.screen = self.env.get_screen()

        qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

        #타이머 생성
        self.qtimer = QTimer(self)
        #타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.game_timer)
        #1초(1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(1000 / 60)

        self.show()

    def update_screen(self):
        #화면 가져오기
        self.screen = self.env.get_screen()
        screen_qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(screen_qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        #pixmap = pixmap.scaled(self.screen_width, self.screen_height, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

    def game_timer(self):
        # 키 배열: B, NULL, SELECT, START, U, D, L, R, A
        # self.env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.env.step(self.press_buttons)
        self.update_screen()
        ram = self.env.get_ram()


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.press_buttons[4] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[5] = 1
        elif key == Qt.Key_Left:
            self.press_buttons[6] = 1
        elif key == Qt.Key_Right:
            self.press_buttons[7] = 1
        elif key == Qt.Key_A:
            self.press_buttons[8] = 1
        elif key == Qt.Key_B:
            self.press_buttons[0] = 1

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.press_buttons[4] = 0
        elif key == Qt.Key_Down:
            self.press_buttons[5] = 0
        elif key == Qt.Key_Left:
            self.press_buttons[6] = 0
        elif key == Qt.Key_Right:
            self.press_buttons[7] = 0
        elif key == Qt.Key_A:
            self.press_buttons[8] = 0
        elif key == Qt.Key_B:
            self.press_buttons[0] = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())