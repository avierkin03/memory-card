from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

window = QWidget()

#віджети, які треба буде розмістити
btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
btn_OK = QPushButton('Відповісти')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
lb_Question = QLabel("")

#Панель з  варіантами відповідей
RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup() #для групування перемикачів

rbtn_1 = QRadioButton("")
rbtn_2 = QRadioButton("")
rbtn_3 = QRadioButton("")
rbtn_4 = QRadioButton("")

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#Розміщуємо варіанти відповідей у 2 стовпці всередниі групи
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()  

layout_ans2.addWidget(rbtn_1)    #2  відповіді у перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)    #2  відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)  

layout_ans1.addLayout(layout_ans2)  #розмістили стопці в одному рядку
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) #готова панель зваріаантами відпоідей


#Панель із результатом
AnsGroupBox =QGroupBox("Результати тесту")
lb_Result = QLabel("") # 'правильно'\'неправильно'
lb_Correct = QLabel("")  #правильна відповідь

#розміщуємо результат
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()


#розміщуємо всі віджети у вікні, вони розташовані в 4 ряди
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) #розрив між кнопками
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("хвилин"))

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)  #кнопка має бути великою
layout_line4.addStretch(1)


#Тепер створені 4 рядки розмістимо один під одним
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  #прогалини між вмістом


#встановлюємо леяут з інтерфейсом у вікно та задаємо розміри вікна
window.setLayout(layout_card)
window.resize(600, 500)
