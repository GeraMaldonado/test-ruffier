from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connection()
    self.show()

  def set_appear(self):
    self.setWindowTitle('Test Ruffier')
    self.resize(500,500)
    self.move(300, 200)

  def initUI(self):
    pass

  def connection(self):
    pass