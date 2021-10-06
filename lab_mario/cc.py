import retro
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import sys
import numpy as np
# 게임 환경 생성
env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
def keyReleaseEvent(self, event):
    key = event.key()
    if key == event.key_Up:
        self.press_buttons[4] = 0
    elif key == event.key_Down:
        self.press_buttons[5] = 0
    elif key == event.key_Left:
        self.press_buttons[6] = 0
    elif key == event.key_Right:
        self.press_buttons[7] = 0
    elif key == Qt.Key_A:
        self.press_buttons[8] = 0
    elif key == Qt.Key_B:
        self.press_buttons[9] = 0
    self.qtimer = QTimer(self)
    # 타이머에 호출할 함수 연결
    self.qtimer.timeout.connect(self.timer)
    # 1초(=1000밀리초)마다 연결된 함수를 실행
    self.qtimer.start(1000)
    def timer(self):
        print('timer')
# 새 게임 시작
env.reset()

# 화면 가져오기
screen = env.get_screen()
# C:\Users\한승엽\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools
print(screen.shape)
print(screen)