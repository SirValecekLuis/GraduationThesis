import sys
import matplotlib
import random

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self):
        fig = Figure()
        super().__init__(fig)
        self.axes = fig.add_subplot(2, 1, 1)
        self.axes2 = fig.add_subplot(2, 1, 2)
        self.toolbar = NavigationToolbar(canvas=self, parent=None)
        self.obrazek, = self.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        self.obrazek2, = self.axes2.plot([0, 1, 2, 3, 4], [1, 6, 2, 6, 3])


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.sc = MplCanvas()
        self.obrazek = self.sc.obrazek

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.sc)
        self.btn = QtWidgets.QPushButton("Tlačítkoooo")
        layout.addWidget(self.btn)
        self.btn.pressed.connect(self.timer)
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.timer)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def timer(self):
        self.time.start(1000)
        data = [random.randint(1, 10) for _ in range(5)]
        second_list = [1, 10, 20, 50, 100]
        self.sc.axes.set_ylim(0, 100)
        self.sc.axes.set_xlim(0, 100)
        self.obrazek.set_data(data, second_list)
        self.obrazek.figure.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
