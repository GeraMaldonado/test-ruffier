from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instr import txt_title, win_x, win_y, win_width, win_height

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connection()
    self.show()

  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def initUI(self):
    pass

  def connection(self):
    pass