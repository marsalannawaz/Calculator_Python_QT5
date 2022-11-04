__author__ = "Muhammad Arsalan Nawaz"
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Calculator.ui", self)
        self.setFixedSize(343, 423)
        
        # Define Our Widgets
        self.buttondot = self.findChild(QPushButton, "pushButton_17")
        self.button0 = self.findChild(QPushButton, "pushButton_19")
        self.button1 = self.findChild(QPushButton, "pushButton_13")
        self.button2 = self.findChild(QPushButton, "pushButton_16")
        self.button3 = self.findChild(QPushButton, "pushButton_14")
        self.button4 = self.findChild(QPushButton, "pushButton_9")
        self.button5 = self.findChild(QPushButton, "pushButton_12")
        self.button6 = self.findChild(QPushButton, "pushButton_10")
        self.button7 = self.findChild(QPushButton, "pushButton_5")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_6")
        self.buttonequal = self.findChild(QPushButton, "pushButton_11")
        self.buttonadd = self.findChild(QPushButton, "pushButton_18")
        self.buttonsubtract= self.findChild(QPushButton, "pushButton_7")
        self.buttonmultiply = self.findChild(QPushButton, "pushButton_4")
        self.buttondivide = self.findChild(QPushButton, "pushButton_3")
        self.buttonback = self.findChild(QPushButton, "pushButton_2")
        self.buttonclear = self.findChild(QPushButton, "pushButton_cl")
        self.screens = self.findChild(QLabel, "screen")


        # Adding action to each of the button
        self.buttondot.clicked.connect(self.clicked_buttondot)
        self.button0.clicked.connect(self.clicked_button0)
        self.button1.clicked.connect(self.clicked_button1)
        self.button2.clicked.connect(self.clicked_button2)
        self.button3.clicked.connect(self.clicked_button3)
        self.button4.clicked.connect(self.clicked_button4)
        self.button5.clicked.connect(self.clicked_button5)
        self.button6.clicked.connect(self.clicked_button6)
        self.button7.clicked.connect(self.clicked_button7)
        self.button8.clicked.connect(self.clicked_button8)
        self.button9.clicked.connect(self.clicked_button9)
        self.buttonequal.clicked.connect(self.clicked_buttonequal)
        self.buttonadd.clicked.connect(self.clicked_buttonadd)
        self.buttonsubtract.clicked.connect(self.clicked_buttonsubtract)
        self.buttonmultiply.clicked.connect(self.clicked_buttonmultiply)
        self.buttondivide.clicked.connect(self.clicked_buttondivide)
        self.buttonback.clicked.connect(self.clicked_buttonback)
        self.buttonclear.clicked.connect(self.clicked_buttonclear)

        self.show()

    def clicked_buttondot (self):
        text = self.screens.text()
        self.screens.setText(text + ".")

    def clicked_button0 (self):
        text = self.screens.text()
        self.screens.setText(text + "0")
        
    def clicked_button1 (self):
        text = self.screens.text()
        self.screens.setText(text + "1")

    def clicked_button2 (self):
        text = self.screens.text()
        self.screens.setText(text + "2")

    def clicked_button3 (self):
        text = self.screens.text()
        self.screens.setText(text + "3")

    def clicked_button4 (self):
        text = self.screens.text()
        self.screens.setText(text + "4")

    def clicked_button5 (self):
        text = self.screens.text()
        self.screens.setText(text + "5")

    def clicked_button6 (self):
        text = self.screens.text()
        self.screens.setText(text + "6")

    def clicked_button7 (self):
        text = self.screens.text()
        self.screens.setText(text + "7")

    def clicked_button8 (self):
        text = self.screens.text()
        self.screens.setText(text + "8")

    def clicked_button9 (self):
        text = self.screens.text()
        self.screens.setText(text + "9")

    def clicked_buttonadd (self):
        text = self.screens.text()
        self.screens.setText(text + "+")

    def clicked_buttonsubtract (self):
        text = self.screens.text()
        self.screens.setText(text + "-")

    def clicked_buttonmultiply (self):
        text = self.screens.text()
        self.screens.setText(text + "*")

    def clicked_buttondivide (self):
        text = self.screens.text()
        self.screens.setText(text + "/")

    def clicked_buttonback (self):
        text = self.screen.text()
        self.screen.setText(text[:len(text)-1])

    def clicked_buttonclear (self):
        self.screens.setText("")

    def clicked_buttonequal (self):
        equation = self.screen.text()
        try:
			# getting the ans
            ans = eval(equation)

			# setting text to the label
            self.screen.setText(str(ans))

        except:
			# setting text to the label
            self.screen.setText("")

app = QApplication(sys.argv)
window = UI()
app.exec_()