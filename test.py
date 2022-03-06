import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot()
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas()
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        sc.axes.plot([1, 2, 3, 4, 5], [12, 13, 14, 15, 16])

        sc.setGeometry(QtCore.QRect(500,500,500,500))

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        self.btn = QtWidgets.QPushButton("Tlačítkoooo")
        layout.addWidget(self.btn)
        self.btn.pressed.connect(self.timer)
        self.label = QtWidgets.QLabel("Tady bude informace")
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.timer)
        layout.addWidget(self.label)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def timer(self):
        self.time.start(1000)
        time = QtCore.QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)
        print("Zopakovano")


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
