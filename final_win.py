from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from instr import *


class FinalWin(QWidget):
  def __init__(self, datos):
    super().__init__()
    self.datos = datos
    self.set_appear()
    self.initUI()
    self.show()

  def set_appear(self):
    self.setWindowTitle(txt_finalwin)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def initUI(self):
    result = self.resutlado() 

    self.txt_index = QLabel(txt_index)
    self.txt_workheart = QLabel(txt_workheart + result)
 
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.txt_index, alignment = Qt.AlignCenter)
    self.layout.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)
    self.setLayout(self.layout)


  def resutlado(self):
    indice = (4 * (self.datos.test1 + self.datos.test2 + self.datos.test3) - 200) / 10

    if self.datos.age <= 6:
        return "No existen resultados para esta edad"

    if self.datos.age >= 15:
        if indice >= 15:
            return txt_res1
        elif indice >= 11 and indice <= 14.9:
            return txt_res2
        elif indice >= 6 and indice <= 10.9:
            return txt_res3
        elif indice >= 0.5 and indice <= 5.9:
            return txt_res4
        elif indice <= 0.4:
            return txt_res5
    elif self.datos.age == 13 or self.datos.age == 14:
        if indice >= 16.5:
            return txt_res1
        elif indice >= 12.5 and indice <= 16.4:
            return txt_res2
        elif indice >= 7.5 and indice <= 12.4:
            return txt_res3
        elif indice >= 2 and indice <= 7.4:
            return txt_res4
        elif indice <= 1.9:
            return txt_res5
    elif self.datos.age == 12:
        if indice >= 18:
            return txt_res1
        elif indice >= 14 and indice <= 17.9:
            return txt_res2
        elif indice >= 9 and indice <= 13.9:
            return txt_res3
        elif indice >= 3.5 and indice <= 8.9:
            return txt_res4
        elif indice <= 3.4:
            return txt_res5
    elif self.datos.age == 9 or self.datos.age == 10:
        if indice >= 19.5:
            return txt_res1
        elif indice >= 15.5 and indice <= 19.4:
            return txt_res2
        elif indice >= 10.5 and indice <= 15.4:
            return txt_res3
        elif indice >= 5 and indice <= 10.4:
            return txt_res4
        elif indice <= 4.9:
            return txt_res5
    elif self.datos.age == 7 or self.datos.age == 8:
        if indice >= 21:
            return txt_res1
        elif indice >= 17 and indice <= 20.9:
            return txt_res2
        elif indice >= 12 and indice <= 16.9:
            return txt_res3
        elif indice >= 6.5 and indice <= 11.9:
            return txt_res4
        elif indice <= 6.4:
            return txt_res5