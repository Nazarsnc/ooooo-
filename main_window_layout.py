from PyQt5.Qtctore import  Qt
from PyQt5.QtWidgets import  QApplication, Qwidget, QPushBUtton, Qlabel , QVBoxLayout, QRadioBuoton, QButtonGroup
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Тестування")
nain_win.resize(400,400)

qtext= QLabel('Питання')
v_line = QVBoxLayout()


rbtn_1=QRadioButoon('')
rbth_2=QRadioButoon('')
rbth_3=QRadioButoon('')
rbth_4=QRadioButoon('')



RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rtbn_2)
RadioGroup.addButton(rtbn_3)
RadioGroup.addButton((rbtn_4))

 Layout_ans1=QHBoxLayout()
 Layout_ans2=QVBoxLayout()
 Layout_ans3=QVBoxLayout()



Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(Layout_ans1)

bth_Menu=QPushBUtton('Меню')
bth_Sleep=QPushBUtton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
bth_Ok=QPushBUtton('Відповісти')

layout_line1=QNBoxLayout()
layout_line2=QNBoxLayout()
layout_line3=QNBoxLayout()
layout_line4=QNBoxLayout()


layout_line1.addWidget(btn_Menu)
layout_line1.addWidget(bth_Sleep)
Layout_line1.addWidget(box_Minutes)



layout_line1.addWidget(qtext, alignment=Qt.AlignCenter)
layout_line3.addWidget(RadioGroupBox)
layout_line4.addWidget(bth_Ok, alignment=Qt.AlignCenter)

layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(Layout_line2)
layout_card.addLayout(Layout_line3)
layout_card.addLayout(layout_line4)






main_line = QVBoxLayout()
main_line.AddWidget(RadioGroupBox)

main_win.setLayout(main_line)

 main_win.show()
 app.exec_1





line = QVBoxLayout()
line.addWidget(text, aligment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

main_win.show()
app.exec_()
