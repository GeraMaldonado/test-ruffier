from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont

from instr import txt_title, win_x, win_y, win_width, win_height, txt_name, txt_hintname, txt_hintage, txt_age, txt_test1, txt_starttest1, txt_hinttest1, txt_test2, txt_starttest2, txt_hinttest2, txt_test3, txt_starttest3, txt_hinttest3, txt_timer

class Datos():
  def __init__(self, name, age, test1, test2, test3):
    self.name = name
    self.age = int(age)
    self.test1 = int(test1)
    self.test2 = int(test2)
    self.test3 = int(test3)

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

      self.test1_inst = QLabel(txt_test1)
      self.test1_button = QPushButton(txt_starttest1)
      self.rest1_result = QLineEdit(txt_hinttest1) 


      self.test2_inst = QLabel(txt_test2)
      self.test2_button = QPushButton(txt_starttest2)
      self.test3_inst = QLabel(txt_test3)
      self.test3_button = QPushButton(txt_starttest3)


      self.rest2_result = QLineEdit(txt_hinttest2) 
      self.rest3_result = QLineEdit(txt_hinttest3)



      self.left_layout = QVBoxLayout()
      self.left_layout.addWidget(self.label_name, alignment = Qt. AlignLeft);
      self.left_layout.addWidget(self.input_name, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.label_age, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.input_age, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.test1_inst, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.test1_button, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.rest1_result, alignment = Qt.AlignLeft)

      self.left_layout.addWidget(self.test2_inst, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.test2_button, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.test3_inst, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.test3_button, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.rest2_result, alignment = Qt.AlignLeft)
      self.left_layout.addWidget(self.rest3_result, alignment = Qt.AlignLeft)


      self.label_time = QLabel(txt_timer) 
      self.label_time.setFont(QFont("Arial", 35, QFont.Bold))


      self.right_layout = QVBoxLayout()
      self.right_layout.addWidget(self.label_time)		


      self.buttom = QPushButton("Siguiente")

      self.h_layaout = QHBoxLayout()
      self.h_layaout.addLayout(self.left_layout)
      self.h_layaout.addLayout(self.right_layout)

      self.main_layout = QVBoxLayout()
      self.main_layout.addLayout(self.h_layaout)
      self.main_layout.addWidget(self.buttom, alignment = Qt.AlignCenter)


      self.setLayout(self.main_layout)


  def connection(self):
    self.test1_button.clicked.connect(self.timer_test)
    self.test2_button.clicked.connect(self.timer_sits)
    self.test3_button.clicked.connect(self.timer_final)
    self.buttom.clicked.connect(self.next_click)



  def next_click(self):
#    self.hide()
#    self.final_win =
    resultados = Datos(self.input_name.text(), self.input_age.text(), self.rest1_result.text(), self.rest2_result.text(), self.rest3_result.text())

  def timer_test(self):
    self.time = QTime(0,0,15)
    self.label_time.setText(self.time.toString())
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer1Event)
    self.timer.start(1000)


  def timer1Event(self):
    self.time = self.time.addSecs(-1)
    self.label_time.setText(self.time.toString())
    if self.time.toString() == "00:00:00":
      self.timer.stop()

  def timer_sits(self):
    self.time = QTime(0,0,30)
    self.label_time.setText(self.time.toString()[6:8])
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer2Event)
    self.timer.start(1500)

  def timer2Event(self):
    self.time = self.time.addSecs(-1)
    self.label_time.setText(self.time.toString()[6:8])
    if self.time.toString() == "00:00:00":
      self.timer.stop()


  def timer_final(self):
    self.time = QTime(0,1,0)
    self.label_time.setText(self.time.toString())
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer3Event)
    self.timer.start(1000)

  def timer3Event(self):
    self.time = self.time.addSecs(-1)
    self.label_time.setText(self.time.toString())
    if self.time.toString() == "00:00:59":
      self.label_time.setStyleSheet("color: rgb(0,255,0)")
    elif self.time.toString() == "00:00:44":
      self.label_time.setStyleSheet("color: rgb(0,0,0)")
    elif self.time.toString() == "00:00:15":
      self.label_time.setStyleSheet("color: rgb(0,255,0)")
    if self.time.toString() == "00:00:00":
      self.timer.stop()