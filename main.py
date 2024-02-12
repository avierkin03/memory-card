from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle, choice
from time import sleep

app = QApplication([])
from main_window import*
from menu_window import*

#клас для запитання
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question # питання
        self.answer = answer # правильна відповідь
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2  
        self.wrong_answer3 = wrong_answer3 
        self.correct = 0       #к-ть правильних відповідей
        self.attempts = 0      #загальна к-ть спроб відповісти

    def got_right(self):
        self.correct += 1
        self.attempts += 1
        print("Це правильна відповідь!")
        
    def got_wrong(self):
        self.attempts += 1
        print("Відповідь неправильна")


#створюємо 4 питання (об'єкти класу Question)
q1 = Question("Яблуко", "apple", 'application', 'apply', "pineaple")
q2 = Question("Дім", "house", "horse", "hurry", "hour")
q3 = Question("Миша", "mouse", "tiger", "mouth", "museum")
q4 = Question("Число", "number", "digit", "amount", "summary")


#список кнопок та список зпитань
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]


#функція, яка відображає нове питання та варіанти відповідей до нього
def new_question():
    global cur_question
    #обираємо рандомне питання
    cur_question = choice(questions)
    lb_Question.setText(cur_question.question)
    lb_Correct.setText(cur_question.answer)
    #перемішуємо радіокнопки
    shuffle(radio_buttons)
    #роставляємо варіанти відповідей
    radio_buttons[0].setText(cur_question.wrong_answer1)
    radio_buttons[1].setText(cur_question.wrong_answer2)
    radio_buttons[2].setText(cur_question.wrong_answer3)
    radio_buttons[3].setText(cur_question.answer)

new_question()


#функція,  яка перевіряє обрану відповідь
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                cur_question.got_right()
                lb_Result.setText("Вірно")
                answer.setChecked(False)
                break
            else:
                lb_Result.setText("Не вірно")
                cur_question.got_wrong()
    RadioGroup.setExclusive(True)


#функція, яка спрацьовую при натисканні на кнопку "Відповісти\Наступне питання"
def click_ok():
    #переключаємося на 'коробку' з результатами
    if btn_OK.text() == "Відповісти":
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText("Наступне запитання")
    #переключаємося на 'коробку' з питаннями
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText("Відповісти")

#підключаємо функцію click_ok() до кнопки "Відповісти\Наступне питання"
btn_OK.clicked.connect(click_ok)


#Функція, яка запускає "Відпочинок"
def rest():
    window.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    window.show()

#підключаємо функцію rest() до кнопки "Відпочити"
btn_Sleep.clicked.connect(rest)


#Фукція, яка відкриває екран меню та ховає головний екран, а також підраховує статистику
def menu_generation():
    if cur_question.attempts == 0:
        success = 0
    else:
        success = (cur_question.correct/cur_question.attempts)*100

    text = f'Разів відповіли: {cur_question.attempts}\n' \
           f'Вірних відповідей: {cur_question.correct}\n' \
           f'Успішність: {round(success, 2)}%'
    lb_statistic.setText(text)
    menu_window.show()
    window.hide()

#підключаємо функцію menu_generation() до кнопки "Меню"
btn_Menu.clicked.connect(menu_generation)


#Фукція, яка відкриває головний екран та ховає меню
def back_menu():
    menu_window.hide()
    window.show()

#підключаємо функцію back_menu() до кнопки "Назад"
btn_back.clicked.connect(back_menu)


#Фукція, яка очищає значення всіх QLineEdit
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

#підключаємо функцію clear() до кнопки "Очистити"
btn_clear.clicked.connect(clear)


#Фукція, яка додає нове запитання до списку питань
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()

#підключаємо функцію add_question() до кнопки "Додати"
btn_add_question.clicked.connect(add_question)


window.show()
app.exec()
