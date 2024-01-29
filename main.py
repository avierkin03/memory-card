from PyQt5.QtWidgets import QApplication
from random import shuffle, choice

app = QApplication([])
from main_window import*

#клас для запитання
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attempts = 0
        self.correct = 0
    def got_right(self):
        self.attempts += 1
        self.correct += 1
    def got_wrong(self):
        self.attempts += 1

#створюємо 4 питання (об'єкти класу Question)
q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

#список кнопок та список запитань
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]

#функція, яка відображає нове питання та варіанти відповідей на нього
def new_question():
    global cur_question
    #обираємо sрандомне питання
    cur_question = choice(questions)
    lb_Question.setText(cur_question.question)
    lb_Correct.setText(cur_question.answer)
    #перемішуємо радіокнопки
    shuffle(radio_buttons)
    #розставляємо варіанти відповідей по кнопкам
    radio_buttons[0].setText(cur_question.wrong_answer1)
    radio_buttons[1].setText(cur_question.wrong_answer2)
    radio_buttons[2].setText(cur_question.wrong_answer3)
    radio_buttons[3].setText(cur_question.answer)

new_question()

#функція, яка спрацьовує при натисканні на кнопку 'Відповісти'\Наступне запитання'
def click_ok():
    #переключаємось на 'коробку' з результатом
    if btn_OK.text() == 'Відповісти':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    #переключаємось на 'коробку' з питанням
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')

#підключаємо функцію click_ok() до кнопки 'Відповісти'\Наступне запитання'
btn_OK.clicked.connect(click_ok)

window.show()
app.exec()
