import retro
import numpy as np
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

# https://datacrystal.romhacking.net/wiki/Super_Mario_Bros.:RAM_map
# 0x0500-0x069F	Current tile (Does not effect graphics)
full_screen_tiles = ram[0x0500:0x069F + 1]

# print(full_screen_tiles.shape)
# print(full_screen_tiles)

full_screen_tile_count = full_screen_tiles.shape[0]

full_screen_page1_tile = full_screen_tiles[:full_screen_tile_count // 2].reshape((13, 16))
full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

print(full_screen_tiles)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창크기 조절
        self.setFixedSize(500, 500)
        # 창제목 설정
        self.setWindowTitle('GA Mario')
        # 창 띄우기
        self.show()


# Empty = 0x00
# Fake = 0x01
# Ground = 0x54
# Top_Pipe1 = 0x12
# Top_Pipe2 = 0x13
# Bottom_Pipe1 = 0x14
# Bottom_Pipe2 = 0x15
# Flagpole_Top =  0x24
# Flagpole = 0x25
# Coin_Block1 = 0xC0
# Coin_Block2 = 0xC1
# Coin = 0xC2
# Breakable_Block = 0x51

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())