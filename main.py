from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle, choice

app = QApplication([])
from main_window import*

class Question():
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

q1 = Question("Яблуко", "apple", "application", "pineapple", "apply")
q2 = Question("Число", "number", "amount", "summary", "tree")

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2]

#функція яка відображає нове питання та варіанти відповідей до нього
def new_question():
    global cur_questions
    cur_questions = choice(questions)
    lb_Question.setText(cur_questions.question)
    lb_Correct.setText(cur_questions.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_questions.wrong_answer1)
    radio_buttons[1].setText(cur_questions.wrong_answer2)
    radio_buttons[2].setText(cur_questions.wrong_answer3)
    radio_buttons[3].setText(cur_questions.answer)

def click_ok():
    if btn_OK.text() == "Відповісти":
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText("Наступне запитання")
    else:
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText("Відповісти")

btn_OK.clicked.connect(click_ok)
    


new_question()







win_card = QWidget()
win_card.resize(600, 500)
win_card.move(300, 300)
win_card.setWindowTitle("Memory Card")

win_card.setLayout(layout_card)


win_card.show()
app.exec()