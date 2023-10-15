from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QApplication, QWidget, QRadioButton, QGroupBox,
    QButtonGroup, QSpinBox, QLineEdit
)

app = QApplication([])
main_win = QWidget()

question_Label = QLabel('Введіть запитанная')
cor_ans_Label = QLabel('Введіть першу відповіть')
answer1_Label = QLabel('Введіть першу хибну відповіть')
answer2_Label = QLabel('Введіть другу хибну відповіть')
answer3_Label = QLabel('Введіть третю хибну відповіть')
estion = QLineEdit()
correct_answer = QLineEdit()

answer1 = QLineEdit()
answer2 = QLineEdit()
answer3 = QLineEdit()

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()


line1.addWiget(question_Label)
line1.addWiget(question)

line2.addWiget(cor_ans_Label)
line2.addWiget(correct_answer)

line3.addWiget(answer1_Label)
line3.addWiget(answer1)

line4.addWiget(answer2_Label)
line4.addWiget(answer2)

line5.addWiget(answer3_Label)
line5.addWiget(answer3)

edit_layout =QHBoxLayout()
edit_layout.addLayout(line1)
edit_layout.addLayout(line2)
edit_layout.addLayout(line3)
edit_layout.addLayout(line4)
edit_layout.addLayout(line5)

btn_add = QPushButton('Додати запитання')
btn_clean = QPushButton('Очистити')
line6 = QHBoxLayout()
line6.addWiget(bth_add)
line6.addWiget(bth_clean)

stat_title = QLabel('Статистика')
amount_atempt = QLabel('Разів відповідей')
amount_correct =QLabel('Вірних відповідей')
sucsessful = QLabel('Успішність')

stat_line = QVBoxLayout()
stat_line.addWidget(stat_title, alignment=Qt.AlignLeft)
stat_line.addWidget(amount_atempt, alignment=Qt.AlignLeft)
stat_line.addWidget(amount_correct, alignment=Qt.AlignLeft)
stat_line.addWidget(sucsessful, alignment=Qt.AlignLeft)

edit_layout.addLayout(stat_line)

btn_back

main_win.setLayout(line1)
main_win.show()
app.exec_()
qu
