from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget,\
     QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QLayout, QCheckBox
from PyQt5.QtCore import Qt

import sys


class TabWidgetForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moc zajímavá applikace")

        self.tab_1 = Tab1()
        self.tab_2 = Tab2()

        self.tab_widget = QTabWidget(self)
        self.tab_widget.addTab(self.tab_1, "Tab 1")
        self.tab_widget.addTab(self.tab_2, "Tab 2")

        self.btn = QPushButton("Ulož údaje")
        # noinspection PyUnresolvedReferences
        self.btn.clicked.connect(self.on_click)

        self.v_box = QVBoxLayout(self)
        self.v_box.addWidget(self.tab_widget)
        self.v_box.addWidget(self.btn)

        self.container = QWidget(self)
        self.container.setLayout(self.v_box)
        self.setCentralWidget(self.container)

        self.studenti = []


    def on_click(self):
        j = self.tab_1.jmeno_edit.text()
        e = self.tab_1.email_edit.text()
        m = self.tab_2.math_check.checkState() == Qt.Checked
        a = self.tab_2.ang_check.checkState() == Qt.Checked

        s = Student(j, e, m, a)
        self.studenti.append(s)

        print(s)

class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.jmeno = QLabel("jmeno", self)
        self.jmeno_edit = QLineEdit(self)
        self.email = QLabel("email", self)
        self.email_edit = QLineEdit(self)

        self.v_box = QHBoxLayout(self)
        self.v_box.addWidget(self.jmeno)
        self.v_box.addWidget(self.jmeno_edit)
        self.v_box.addWidget(self.email)
        self.v_box.addWidget(self.email_edit)
        self.setLayout(self.v_box)


class Tab2(QWidget):
    def __init__(self):
        super(Tab2, self).__init__()
        self.math_check = QCheckBox("Matematika", self)
        self.ang_check = QCheckBox("Angličtina", self)

        self.h_box = QHBoxLayout(self)
        self.h_box.addWidget(self.math_check)
        self.h_box.addWidget(self.ang_check)
        self.setLayout(self.h_box)

class Student:
    def __init__(self, jmeno, email, math, ang):
        self.jmeno = jmeno
        self.email = email
        self.math = math
        self.ang = ang

    def __str__(self):
        return f"{self.jmeno}, {self.email}, {self.math}, {self.ang}. "



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TabWidgetForm()
    win.show()
    sys.exit(app.exec_())