
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication, QLineEdit
from instr import txt_title, win_x, win_y, win_width, win_height, txt_name, txt_hintname, txt_hintage, txt_age

class TestWin(QWidget):
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
     
      self.label_name = QLabel(txt_name)
      self.input_name = QLineEdit(txt_hintname)
      self.label_age = QLabel(txt_age)
      self.input_age = QLineEdit(txt_hintage)

      self.left_layout = QVBoxLayout()
      self.left_layout.addWidget(self.label_name, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.input_name, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.label_age, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.input_age, alignment = Qt.AlignLeft)

      self.setLayout(self.left_layout)


  def connection(self):
  	pass
    


  def next_click(self):
    #mostrar sigueinte venta
    self.hide()
