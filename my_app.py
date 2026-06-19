from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication
from instr import txt_title, win_x, win_y, win_width, win_height, txt_hello, txt_instruction, txt_next

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
    self.hello_text = QLabel(txt_hello)
    self.instructions = QLabel(txt_instruction)
    self.button = QPushButton(txt_next)
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.hello_text)
    self.layout.addWidget(self.instructions)
    self.layout.addWidget(self.button, alignment = Qt.AlignCenter) 
    self.setLayout(self.layout)

  def connection(self):
    self.button.clicked.connect(self.next_click)


  def next_click(self):
    #mostrar sigueinte venta
    self.hide()



app = QApplication([])
mw = MainWin()
app.exec_()