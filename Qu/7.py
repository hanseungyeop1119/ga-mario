import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(400, 300)
        # 창 제목 설정
        self.setWindowTitle('GA Mario')

        self.i = 0
        self.label = QLabel(self)
        # 타이머 생성
        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        # 1초(=1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(1000)

        # 창 띄우기
        self.show()

    def timer(self):
        self.label.setGeometry(100, 100, 100, 100)
        self.label.setText(str(self.i))
        self.i = self.i + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())