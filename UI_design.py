from PyQt5 import QtCore, QtGui, QtWidgets
from temp_backend import HWMInit, CPU, GPU, File, Graph
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  # Toolbar pro Canvas
import os


class UIMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Základní nastavení okna
        self.setMinimumSize(0, 0)
        self.setMaximumSize(1024, 768)
        self.setGeometry(400, 150, 1024, 768)

        # 1. tab
        self.tab_1 = QtWidgets.QWidget()
        self.q_tab1 = QtWidgets.QTabWidget()
        self.CPU_MAIN_LABEL = QtWidgets.QLabel(self.tab_1)
        self.GPU_MAIN_LABEL = QtWidgets.QLabel(self.tab_1)

        # Slouží k odstranění HTML textu a zpětného přidání
        self.parse_func = lambda text: text.replace(self.html_text_head, "").replace(self.html_font_end, "")
        self.font_func = lambda text: self.html_text_head + text + self.html_font_end

        # Fonty
        self.html_title_head = "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">"
        self.html_small_title_head = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"
        self.html_font_end = "</span></p></body></html>"
        self.html_text_head = "<html><head/><body><p><span style=\" font-size:12pt;\">"

        # CPU - označené věci křížkem znamenají, že se nastaví pouze jedenkrát
        self.cpu_frequency_label = QtWidgets.QLabel(self.tab_1)  #
        self.cpu_name_label = QtWidgets.QLabel(self.tab_1)  #
        self.cpu_cores_label = QtWidgets.QLabel(self.tab_1)  #
        self.cpu_actual_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_min_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_max_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_load_label = QtWidgets.QLabel(self.tab_1)

        # GPU - označené věci křížkem znamenají, že se nastaví pouze jedenkrát
        self.gpu_name_label = QtWidgets.QLabel(self.tab_1)  #
        self.gpu_total_memory_label = QtWidgets.QLabel(self.tab_1)  #
        self.gpu_memory_used_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_fan_load_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_min_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_max_temp_label = QtWidgets.QLabel(self.tab_1)
        # Konec 1. tabu

        # Čáry
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line_2 = QtWidgets.QFrame(self.tab_1)
        self.line_3 = QtWidgets.QFrame(self.tab_1)
        self.line_4 = QtWidgets.QFrame(self.tab_1)
        self.line_5 = QtWidgets.QFrame(self.tab_1)
        self.line_6 = QtWidgets.QFrame(self.tab_1)
        self.line_7 = QtWidgets.QFrame(self.tab_1)
        self.line_8 = QtWidgets.QFrame(self.tab_1)
        self.line_9 = QtWidgets.QFrame(self.tab_1)
        self.line_10 = QtWidgets.QFrame(self.tab_1)
        self.line_11 = QtWidgets.QFrame(self.tab_1)
        self.line_12 = QtWidgets.QFrame(self.tab_1)
        self.line_13 = QtWidgets.QFrame(self.tab_1)
        self.line_14 = QtWidgets.QFrame(self.tab_1)
        self.line_15 = QtWidgets.QFrame(self.tab_1)
        self.line_16 = QtWidgets.QFrame(self.tab_1)
        self.line_17 = QtWidgets.QFrame(self.tab_1)
        self.line_18 = QtWidgets.QFrame(self.tab_1)
        self.line_19 = QtWidgets.QFrame(self.tab_1)
        # Konec čar

        # Začátek 2. tabu
        self.tab_2 = QtWidgets.QWidget()
        self.CPU_WIDGET = QtWidgets.QWidget(self.tab_2)
        self.GPU_WIDGET = QtWidgets.QWidget(self.tab_2)
        self.CPU_LAYOUT = QtWidgets.QVBoxLayout(self.CPU_WIDGET)
        self.GPU_LAYOUT = QtWidgets.QVBoxLayout(self.GPU_WIDGET)
        self.pause_graphs_btn = QtWidgets.QPushButton(self.tab_2)
        self.resume_graphs_btn = QtWidgets.QPushButton(self.tab_2)
        self.resume_graphs_btn.setEnabled(False)
        self.gpu_temp_btn = QtWidgets.QPushButton(self.tab_2)
        self.gpu_fan_btn = QtWidgets.QPushButton(self.tab_2)
        self.gpu_memory_btn = QtWidgets.QPushButton(self.tab_2)
        self.cpu_temp_btn = QtWidgets.QPushButton(self.tab_2)
        self.cpu_load_btn = QtWidgets.QPushButton(self.tab_2)
        self.LABEL_INFO = QtWidgets.QLabel(self.tab_2)
        self.label_time = QtWidgets.QLabel(self.tab_2)
        self.label_data_amount = QtWidgets.QLabel(self.tab_2)
        self.LABEL_GPU = QtWidgets.QLabel(self.tab_2)
        self.LABEL_CPU = QtWidgets.QLabel(self.tab_2)
        # Konec 2. tabu

        # Datová část
        self.computer_object = HWMInit()
        self.file = File("data.csv")
        self.cpu = CPU(self.computer_object.cpu_object)
        self.gpu = GPU(self.computer_object.gpu_object)
        if not os.path.exists("data.csv"):  # Pokud spouštím aplikaci po 1. nebo soubor neexistuje, zapíšu data
            self.file.write_data(self.cpu, self.gpu)
            self.file.update_ndar_list()
        else:
            self.file.update_ndar_list()
        # Konec datové části

        # Nastavení ikony
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Funkce s nastavením
        self._setup_ui()

        # Text k labelům
        self.CPU_ACTUAL_TEMPERATURE_TEXT = self.parse_func(self.cpu_actual_temperature_label.text())
        self.CPU_MIN_TEMPERATURE_TEXT = self.parse_func(self.cpu_min_temperature_label.text())
        self.CPU_MAX_TEMPERATURE_TEXT = self.parse_func(self.cpu_max_temperature_label.text())
        self.CPU_LOAD_TEXT = self.parse_func(self.cpu_load_label.text())
        self.GPU_MEMORY_USED_TEXT = self.parse_func(self.gpu_memory_used_label.text())
        self.GPU_FAN_LOAD_TEXT = self.parse_func(self.gpu_fan_load_label.text())
        self.GPU_TEMPERATURE_TEXT = self.parse_func(self.gpu_temperature_label.text())
        self.GPU_MIN_TEMPERATURE_TEXT = self.parse_func(self.gpu_min_temperature_label.text())
        self.GPU_MAX_TEMP_TEXT = self.parse_func(self.gpu_max_temp_label.text())

        self.TIME_TEXT = self.parse_func(self.label_time.text())
        self.DATA_AMOUNT_TEXT = self.parse_func(self.label_data_amount.text())

        # Timer pro opakovaní a hlavní spuštění aplikace
        self.timer = QtCore.QTimer()
        self.update_graphs_bool = True
        self._set_labels()
        self._show_graphs()
        self._run()
        self.timer.timeout.connect(self._run)

    def _setup_ui(self):
        """
        setup_ui slouží k nastavení pozic a hodnot pro veškeré Widgety
        Proměnné psané tiskacím by neměly být upravovány
        """

        # Nastavení 1. tabu
        self.q_tab1.setGeometry(QtCore.QRect(-2, 0, 1032, 772))
        self.q_tab1.setStyleSheet("background-color: rgb(211, 211, 211);")

        self.line.setGeometry(QtCore.QRect(0, 380, 475, 8))
        self.line.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.CPU_MAIN_LABEL.setGeometry(QtCore.QRect(35, 15, 165, 45))
        self.CPU_MAIN_LABEL.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CPU_MAIN_LABEL.setTextFormat(QtCore.Qt.AutoText)

        self.GPU_MAIN_LABEL.setGeometry(QtCore.QRect(35, 395, 191, 45))
        self.GPU_MAIN_LABEL.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.GPU_MAIN_LABEL.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.cpu_frequency_label.setGeometry(QtCore.QRect(55, 150, 231, 21))
        self.cpu_frequency_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_frequency_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_frequency_label.setTextFormat(QtCore.Qt.AutoText)

        self.cpu_cores_label.setGeometry(QtCore.QRect(55, 110, 161, 21))
        self.cpu_cores_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_cores_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_cores_label.setTextFormat(QtCore.Qt.AutoText)

        self.cpu_name_label.setGeometry(QtCore.QRect(55, 70, 411, 21))
        self.cpu_name_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_name_label.setTextFormat(QtCore.Qt.AutoText)

        self.cpu_min_temperature_label.setGeometry(QtCore.QRect(55, 230, 261, 21))
        self.cpu_min_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_min_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_min_temperature_label.setTextFormat(QtCore.Qt.AutoText)

        self.cpu_max_temperature_label.setGeometry(QtCore.QRect(55, 270, 261, 21))
        self.cpu_max_temperature_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cpu_max_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_max_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_max_temperature_label.setTextFormat(QtCore.Qt.AutoText)

        self.cpu_load_label.setGeometry(QtCore.QRect(55, 310, 261, 21))
        self.cpu_load_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_load_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_load_label.setTextFormat(QtCore.Qt.AutoText)

        self.gpu_name_label.setGeometry(QtCore.QRect(55, 455, 411, 21))
        self.gpu_name_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_name_label.setTextFormat(QtCore.Qt.AutoText)

        self.gpu_total_memory_label.setGeometry(QtCore.QRect(55, 495, 261, 21))
        self.gpu_total_memory_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_total_memory_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_total_memory_label.setTextFormat(QtCore.Qt.AutoText)

        self.gpu_memory_used_label.setGeometry(QtCore.QRect(55, 655, 301, 21))
        self.gpu_memory_used_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_memory_used_label.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.gpu_fan_load_label.setGeometry(QtCore.QRect(55, 695, 311, 21))
        self.gpu_fan_load_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_fan_load_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_fan_load_label.setTextFormat(QtCore.Qt.AutoText)

        self.gpu_temperature_label.setGeometry(QtCore.QRect(55, 535, 261, 21))
        self.gpu_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_temperature_label.setTextFormat(QtCore.Qt.AutoText)

        self.gpu_min_temperature_label.setGeometry(QtCore.QRect(55, 575, 291, 21))
        self.gpu_min_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_min_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_min_temperature_label.setTextFormat(QtCore.Qt.AutoText)

        self.cpu_actual_temperature_label.setGeometry(QtCore.QRect(55, 190, 261, 21))
        self.cpu_actual_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_actual_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_actual_temperature_label.setTextFormat(QtCore.Qt.AutoText)

        self.gpu_max_temp_label.setGeometry(QtCore.QRect(55, 615, 271, 21))
        self.gpu_max_temp_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_max_temp_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_max_temp_label.setTextFormat(QtCore.Qt.AutoText)

        # Čáry GUI
        self.line_2.setGeometry(QtCore.QRect(55, 300, 420, 3))
        self.line_2.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_3.setGeometry(QtCore.QRect(55, 180, 420, 3))
        self.line_3.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_4.setGeometry(QtCore.QRect(55, 140, 420, 3))
        self.line_4.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_5.setGeometry(QtCore.QRect(55, 100, 420, 3))
        self.line_5.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_6.setGeometry(QtCore.QRect(55, 220, 420, 3))
        self.line_6.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_7.setGeometry(QtCore.QRect(55, 260, 420, 3))
        self.line_7.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_8.setGeometry(QtCore.QRect(55, 340, 420, 3))
        self.line_8.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_9.setGeometry(QtCore.QRect(55, 485, 420, 3))
        self.line_9.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_10.setGeometry(QtCore.QRect(55, 525, 420, 3))
        self.line_10.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_11.setGeometry(QtCore.QRect(55, 565, 420, 3))
        self.line_11.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_12.setGeometry(QtCore.QRect(55, 605, 420, 3))
        self.line_12.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_13.setGeometry(QtCore.QRect(55, 645, 420, 3))
        self.line_13.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_14.setGeometry(QtCore.QRect(55, 685, 420, 3))
        self.line_14.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_15.setGeometry(QtCore.QRect(55, 725, 420, 3))
        self.line_15.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_16.setGeometry(QtCore.QRect(0, 440, 475, 3))
        self.line_16.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_17.setGeometry(QtCore.QRect(0, 60, 475, 3))
        self.line_17.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_18.setGeometry(QtCore.QRect(475, 60, 3, 283))
        self.line_18.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_19.setGeometry(QtCore.QRect(475, 440, 3, 288))
        self.line_19.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Konec nastavení čar

        # Nastavení 1. tabu
        self.q_tab1.addTab(self.tab_1, "")

        # Odtud začíná nastavení 2. tabu

        self.CPU_WIDGET.setGeometry(QtCore.QRect(470, 40, 521, 301))
        self.GPU_WIDGET.setGeometry(QtCore.QRect(470, 400, 521, 301))
        self.CPU_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.GPU_LAYOUT.setContentsMargins(0, 0, 0, 0)

        self.pause_graphs_btn.setGeometry(QtCore.QRect(140, 535, 101, 23))
        self.resume_graphs_btn.setGeometry(QtCore.QRect(30, 535, 101, 23))

        self.pause_graphs_btn.clicked.connect(self._pause_resume_graphs)
        self.resume_graphs_btn.clicked.connect(self._pause_resume_graphs)

        self.gpu_temp_btn.setGeometry(QtCore.QRect(30, 680, 101, 21))
        self.gpu_fan_btn.setGeometry(QtCore.QRect(301, 680, 131, 21))
        self.gpu_memory_btn.setGeometry(QtCore.QRect(140, 680, 151, 21))
        self.cpu_temp_btn.setGeometry(QtCore.QRect(30, 321, 101, 21))
        self.cpu_load_btn.setGeometry(QtCore.QRect(140, 321, 101, 21))

        self.gpu_temp_btn.clicked.connect(self._update_graphs)
        self.gpu_fan_btn.clicked.connect(self._update_graphs)
        self.gpu_memory_btn.clicked.connect(self._update_graphs)
        self.cpu_temp_btn.clicked.connect(self._update_graphs)
        self.cpu_load_btn.clicked.connect(self._update_graphs)

        self.LABEL_INFO.setGeometry(QtCore.QRect(30, 30, 401, 161))
        self.LABEL_INFO.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        self.label_time.setGeometry(QtCore.QRect(30, 460, 221, 31))
        self.label_data_amount.setGeometry(QtCore.QRect(30, 491, 221, 31))
        self.LABEL_GPU.setGeometry(QtCore.QRect(30, 640, 321, 31))
        self.LABEL_CPU.setGeometry(QtCore.QRect(30, 281, 321, 31))

        self.q_tab1.addTab(self.tab_2, "")
        self.q_tab1.setCurrentIndex(0)
        self.setCentralWidget(self.q_tab1)

        # Nastavení CSS
        self._style_sheet()

    def _style_sheet(self):
        """Nastavování HTML stylů pro každý text"""

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main_window", "Ukazatel teplot"))

        self.CPU_MAIN_LABEL.setText(_translate("main_window", f"{self.html_title_head}CPU - procesor"
                                                              f"{self.html_font_end}")
                                    )
        self.GPU_MAIN_LABEL.setText(_translate("main_window",
                                               f"{self.html_title_head}GPU - grafický čip{self.html_font_end}"))
        self.cpu_frequency_label.setText(_translate("main_window",
                                                    f"{self.html_text_head}Frekvence procesoru MHz: "
                                                    f"{self.html_font_end}")
                                         )
        self.cpu_cores_label.setText(_translate("main_window",
                                                f"{self.html_text_head}Počet jader: {self.html_font_end}"))
        self.cpu_name_label.setText(_translate("main_window",
                                               f"{self.html_text_head}Název procesoru: {self.html_font_end}")
                                    )
        self.cpu_min_temperature_label.setText(_translate("main_window",
                                                          f"{self.html_text_head}Nejmenší naměřená teplota °C: "
                                                          f" {self.html_font_end}")
                                               )
        self.cpu_max_temperature_label.setText(_translate("main_window",
                                                          f"{self.html_text_head}Největší naměřená teplota °C: "
                                                          f" {self.html_font_end}")
                                               )
        self.cpu_load_label.setText(_translate("main_window",
                                               f"{self.html_text_head}Aktuální zátěž procesoru %: "
                                               f"{self.html_font_end}")
                                    )
        self.gpu_name_label.setText(_translate("main_window",
                                               f"{self.html_text_head}Název grafické karty: {self.html_font_end}"))
        self.gpu_total_memory_label.setText(_translate("main_window",
                                                       f"{self.html_text_head}Celkové množství VRAM MB: "
                                                       f"{self.html_font_end}")
                                            )
        self.gpu_memory_used_label.setText(_translate("main_window",
                                                      f"{self.html_text_head}Aktuální vytížení paměti VRAM %: "
                                                      f"{self.html_font_end}")
                                           )
        self.gpu_fan_load_label.setText(_translate("main_window",
                                                   f"{self.html_text_head}Zatížení větráčků na grafické kartě %: "
                                                   f"{self.html_font_end}")
                                        )
        self.gpu_temperature_label.setText(_translate("main_window",
                                                      f"{self.html_text_head}Aktuální teplota C°: "
                                                      f"{self.html_font_end}")
                                           )
        self.gpu_min_temperature_label.setText(_translate("main_window",
                                                          f"{self.html_text_head}Nejmenší naměřená teplota °C: "
                                                          f"{self.html_font_end}")
                                               )
        self.cpu_actual_temperature_label.setText(_translate("main_window",
                                                             f"{self.html_text_head}Aktuální teplota °C: "
                                                             f"{self.html_font_end}")
                                                  )
        self.gpu_max_temp_label.setText(_translate("main_window",
                                                   f"{self.html_text_head}Největší naměřená teplota °C: "
                                                   f"{self.html_font_end}")
                                        )

        self.q_tab1.setTabText(self.q_tab1.indexOf(self.tab_1), _translate("main_window", "Senzory"))

        self.resume_graphs_btn.setText(_translate("main_window", "Spustit grafy"))
        self.pause_graphs_btn.setText(_translate("main_window", "Zastavit grafy"))

        self.gpu_temp_btn.setText(_translate("main_window", "Teplota GPU"))
        self.gpu_fan_btn.setText(_translate("main_window", "Větráčky na GPU"))
        self.gpu_memory_btn.setText(_translate("main_window", "Vytížení paměti VRAM"))
        self.cpu_temp_btn.setText(_translate("main_window", "Teplota CPU"))
        self.cpu_load_btn.setText(_translate("main_window", "Zatížení CPU"))

        self.LABEL_INFO.setText(_translate("main_window", f"{self.html_small_title_head}"
                                                          f"Grafy znázorňující informace v závislosti na čase."
                                                          f"{self.html_text_head}"
                                                          f"Pro výběr stačí pomocí tlačítka vybrat dané"
                                                          f"{self.html_text_head}"
                                                          f"informace, které se mají na ose Y zobrazit."
                                                          f"<br/><br/>Osa X je popsaná časově, každá aktualizace"
                                                          f"{self.html_text_head}"
                                                          f"probíhá po 1s.{self.html_font_end}"))

        self.label_time.setText(_translate("main_window",
                                           f"{self.html_text_head}Délka měření: {self.html_font_end}"))
        self.label_data_amount.setText(_translate("main_window",
                                                  f"{self.html_text_head}Počet sekvencí: {self.html_font_end}"))
        self.LABEL_GPU.setText(_translate("main_window",
                                          f"{self.html_small_title_head}Nastavení osy Y pro GPU:{self.html_font_end}"))
        self.LABEL_CPU.setText(_translate("main_window",
                                          f"{self.html_small_title_head}Nastavení osy Y pro CPU:{self.html_font_end}"))

        self.button_css = """
        QPushButton{
            color: white;
            background: #0577a8;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            font-size: 8pt;
            outline: none;
        }
        
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #0892D0;
        }
        """

        self.button_pause_css = """
        QPushButton{
        color:white;
        background: #a81f1f;
        padding: 5px 10px;
        border-radius: 2px;
        font-weight: bold;
        font-size: 8pt;
        outline: none;
        }
        
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #c90303;
        }
        """

        self.button_resume_css = """
        QPushButton{
        color:white;
        background: #26a14d;
        padding: 5px 10px;
        border-radius: 2px;
        font-weight: bold;
        font-size: 8pt;
        outline: none;
        }
        
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #05c241;
        }
        """

        self.cpu_load_btn.setStyleSheet(self.button_css)
        self.cpu_load_btn.setToolTip("Zobrazí zatížení procesoru")
        self.cpu_temp_btn.setStyleSheet(self.button_css)
        self.cpu_temp_btn.setToolTip("Zobrazí teplotu procesoru")
        self.gpu_fan_btn.setStyleSheet(self.button_css)
        self.gpu_fan_btn.setToolTip("Zobrazí zatížení větráčků")
        self.gpu_memory_btn.setStyleSheet(self.button_css)
        self.gpu_memory_btn.setToolTip("Zobrazí vytížení paměti VRAM")
        self.gpu_temp_btn.setStyleSheet(self.button_css)
        self.gpu_temp_btn.setToolTip("Zobrazí teplotu grafické karty")

        self.resume_graphs_btn.setStyleSheet(self.button_resume_css)
        self.resume_graphs_btn.setToolTip("Vykreslí znovu grafy, pokud jsou pozastaveny")
        self.pause_graphs_btn.setStyleSheet(self.button_pause_css)
        self.pause_graphs_btn.setToolTip("Pozastaví grafy pro práci s grafem")

        self.q_tab1.setTabText(self.q_tab1.indexOf(self.tab_2), _translate("main_window", "Grafy"))

    def _set_labels(self):
        """Funkce slouží k nastavení všech labelů v 1. tabu"""

        # CPU část
        self.cpu_name_label.setText(self.font_func(self.parse_func(self.cpu_name_label.text()) + self.cpu.name))
        self.cpu_cores_label.setText(self.font_func(self.parse_func(self.cpu_cores_label.text()) + self.cpu.cores))
        self.cpu_frequency_label.setText(self.font_func(self.parse_func(self.cpu_frequency_label.text())
                                                        + str(self.cpu.frequency)))

        # GPU část
        self.gpu_name_label.setText(self.font_func(self.parse_func(self.gpu_name_label.text())
                                                   + self.gpu.name))
        self.gpu_total_memory_label.setText(self.font_func(self.parse_func(self.gpu_total_memory_label.text())
                                                           + str(self.gpu.memory_total)))

    def _set_changing_labels(self):
        """Tato funkce slouží k pravidelné obměně informací na 1. tabu, jelikož tyto informace nejsou konstatní"""

        # Pokračování CPU části, která se mění
        self.cpu_actual_temperature_label.setText(
            self.font_func(self.CPU_ACTUAL_TEMPERATURE_TEXT + str(self.cpu.temperature)))
        self.cpu_min_temperature_label.setText(
            self.font_func(self.CPU_MIN_TEMPERATURE_TEXT + str(self.cpu.lowest_temp)))
        self.cpu_max_temperature_label.setText(
            self.font_func(self.CPU_MAX_TEMPERATURE_TEXT + str(self.cpu.highest_temp)))
        self.cpu_load_label.setText(
            self.font_func(self.CPU_LOAD_TEXT + str(self.cpu.load)))

        # Pokračování GPU části, která se mění
        self.gpu_temperature_label.setText(
            self.font_func(self.GPU_TEMPERATURE_TEXT + str(self.gpu.temperature)))
        self.gpu_min_temperature_label.setText(
            self.font_func(self.GPU_MIN_TEMPERATURE_TEXT + str(self.gpu.lowest_temp)))
        self.gpu_max_temp_label.setText(
            self.font_func(self.GPU_MAX_TEMP_TEXT + str(self.gpu.highest_temp)))
        self.gpu_memory_used_label.setText(
            self.font_func(self.GPU_MEMORY_USED_TEXT + str(self.gpu.memory_used)))
        self.gpu_fan_load_label.setText(
            self.font_func(self.GPU_FAN_LOAD_TEXT + str(self.gpu.fan)))

        # Aktualizace labelů a času + velikost souboru
        secs = lines = len(self.file.ndar_list[0]) - 1  # Počet řádků odpovídá počtu sekund
        mins, secs = divmod(secs, 60)
        hours, mins = divmod(mins, 60)

        self.label_time.setText(self.font_func(self.TIME_TEXT + f"{hours}h {mins}m {secs}s"))
        self.label_data_amount.setText(self.font_func(self.DATA_AMOUNT_TEXT + str(lines)))

    def _pause_resume_graphs(self):
        """Slouží k pozastavení, nebo spuštění grafů na základě stisknutého tlačítka"""

        if self.sender() == self.resume_graphs_btn:  # Pokud kliknu na tlačítko vykreslování grafů
            self.update_graphs_bool = True
            self.pause_graphs_btn.setEnabled(True)
            self.resume_graphs_btn.setEnabled(False)
        else:  # Pokud kliknu na tlačítko pozastavení vykreslování grafů
            self.update_graphs_bool = False
            self.pause_graphs_btn.setEnabled(False)
            self.resume_graphs_btn.setEnabled(True)

    def _show_graphs(self):
        """Tato funkce slouží k zobrazení grafů v 2. tabu"""

        del NavigationToolbar.toolitems[-2:]  # Smažu tlačítko pro uložení, shazovalo aplikaci + oddělovník
        # Pro více informací print(NavigationToolbar.toolitems) - output je list

        self.canvas_cpu = Graph(self.file.ndar_list[0:2], self.file.header[0:2])
        toolbar = NavigationToolbar(self.canvas_cpu, self)
        self.CPU_LAYOUT.addWidget(toolbar)
        self.CPU_LAYOUT.addWidget(self.canvas_cpu)

        self.canvas_gpu = Graph(self.file.ndar_list[2:], self.file.header[2:])
        toolbar2 = NavigationToolbar(self.canvas_gpu, self)
        self.GPU_LAYOUT.addWidget(toolbar2)
        self.GPU_LAYOUT.addWidget(self.canvas_gpu)

        self.index_cpu = 1  # Teplota je 2. v csv
        self.index_gpu = 0  # Teplota je 3. v csv (ale začínám od 3. sloupce, takže je to nultá věc)

    def _update_graphs(self):
        """Tato funkce slouží k tomu, když uživatel si přeje zobrazit jiný graf, nebo k aktualizaci stávajícího grafu"""

        dict_btn = {self.cpu_load_btn: 0, self.cpu_temp_btn: 1, self.gpu_temp_btn: 2, self.gpu_fan_btn: 3,
                    self.gpu_memory_btn: 4
                    }  # Slovník s tlačítky a jejich indexy odpovídající CSV souborům
        try:
            index = dict_btn[self.sender()]  # Když je stisknuto tlačítko, najdu ho v listu a připíšu mu index
        except KeyError:
            index = -1  # Když tlačítko nebylo stisknuto, nechávám pozice jak byly

        if 0 <= index <= 1:
            self.index_cpu = index
        elif index >= 2:
            self.index_gpu = index - 2  # Odečítám 2, protože nezačínám od 2 ale od 0, mám jenom část listu

        self.canvas_cpu.update_data(self.file.ndar_list[0:2], self.index_cpu)  # Dodávám index aktuálního csv souboru
        self.canvas_gpu.update_data(self.file.ndar_list[2:], self.index_gpu)  # _,,_

    def _run(self):
        """Funkce slouží k hlavnímu chodu, opakuje se každou sekundu"""

        self.timer.start(1000)
        self.computer_object.update()
        self.cpu = CPU(self.computer_object.cpu_object)
        self.gpu = GPU(self.computer_object.gpu_object)
        self.file.write_data(self.cpu, self.gpu)
        self.file.update_ndar_list()
        self._set_changing_labels()
        if self.update_graphs_bool:  # Pokud není pozastavena aktualizace grafů, tak aktualizuji graf
            self._update_graphs()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UIMainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
