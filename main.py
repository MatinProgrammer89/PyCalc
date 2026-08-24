from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from logic import evaluate_expression,calculate_sqrt,clear_expression,format_number
import sys,os


class Calculator_app(QDialog):

    def __init__(self):

        super().__init__()

        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        uic.loadUi(os.path.join(base_path, "ui", "main.ui"), self)

        self.setWindowIcon(QIcon(os.path.join(base_path, "icon", "main_icon.ico")))

        self.setWindowTitle("Matin Calculaor")

        self.btn_0.clicked.connect(lambda: self.add_to_display("0"))
        self.btn_1.clicked.connect(lambda: self.add_to_display("1"))
        self.btn_2.clicked.connect(lambda: self.add_to_display("2"))
        self.btn_3.clicked.connect(lambda: self.add_to_display("3"))
        self.btn_4.clicked.connect(lambda: self.add_to_display("4"))
        self.btn_5.clicked.connect(lambda: self.add_to_display("5"))
        self.btn_6.clicked.connect(lambda: self.add_to_display("6"))
        self.btn_7.clicked.connect(lambda: self.add_to_display("7"))
        self.btn_8.clicked.connect(lambda: self.add_to_display("8"))
        self.btn_9.clicked.connect(lambda: self.add_to_display("9"))
        self.btn_000.clicked.connect(lambda: self.add_to_display("000"))
        self.btn_auditor.clicked.connect(lambda: self.add_to_display("."))
        self.btn_add.clicked.connect(lambda: self.add_to_display("+"))
        self.btn_sub.clicked.connect(lambda: self.add_to_display("-"))
        self.btn_mul.clicked.connect(lambda: self.add_to_display("*"))
        self.btn_div.clicked.connect(lambda: self.add_to_display("/"))
        self.btn_percent.clicked.connect(lambda: self.add_to_display("%"))



        self.btn_equal.clicked.connect(self.calculate_result)
        self.btn_clear.clicked.connect(self.clear_display)
        self.btn_sqrt.clicked.connect(self.calculator_sqrt)
        self.btn_history.clicked.connect(self.show_history)

        self.result_shown = False

        self.history = []

    
    def add_to_display(self,value):

        if self.result_shown:

            self.display.setText("")

            self.result_shown = False
        
        current = self.display.text().replace(",", "") 
        
        new_expression = current + value

        if new_expression.replace(".", "").isdigit():

            formatted = "{:,}".format(float(new_expression)) if "." in new_expression else "{:,}".format(int(new_expression))

            self.display.setText(formatted)

        else:

            self.display.setText(new_expression)

    
    def calculate_result(self):

        expression = self.display.text().replace(",","")
        result = evaluate_expression(expression)
        self.display.setText(format_number(result))

        self.history.append(f"{expression} = {result}")
    
    def calculator_sqrt(self):

        try:

            number = float(self.display.text())

            result = calculate_sqrt(number)

            self.display.setText(format_number(result))

            self.history.append(f"✓{number} = {result}")

        except:

            self.display.setText("Error")
    
    def clear_display(self):

        self.display.setText(clear_expression())
    
    def show_history(self):

        if self.history:

            self.history_window = History_window(self.history)

            self.history_window.show()
        
        else:

            self.history_window = History_window(["No calculations have been done!"])
            self.history_window.show()

class History_window(QDialog):

    def __init__(self,history_list):

        super().__init__()
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        uic.loadUi(os.path.join(base_path, "ui", "history.ui"), self)

        self.setWindowIcon(QIcon(os.path.join(base_path, "icon", "history_icon.ico")))
        
        self.text_area.setText("\n".join(history_list))

        self.btn_clear_history.clicked.connect(self.clear_history)

    def clear_history(self):

        self.text_area.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator_app()
    window.show()
    app.exec_()