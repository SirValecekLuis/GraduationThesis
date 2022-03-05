from PyQt5 import QtCore, QtGui, QtWidgets


class UIMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("main_window")
        self.setMinimumSize(0, 0)
        self.setMaximumSize(1024, 768)
        self.setGeometry(400, 150, 1024, 768)

        self.tab_1 = QtWidgets.QWidget()
        self.q_tab1 = QtWidgets.QTabWidget()
        self.CPU_MAIN_LABEL = QtWidgets.QLabel(self.tab_1)
        self.GPU_MAIN_LABEL = QtWidgets.QLabel(self.tab_1)
        self.cpu_frequency_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_cores_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_name_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_min_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_max_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_load_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_name_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_total_memory_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_memory_used_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_fan_load_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_min_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.cpu_actual_temperature_label = QtWidgets.QLabel(self.tab_1)
        self.gpu_max_temp_label = QtWidgets.QLabel(self.tab_1)
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
        self.tab_2 = QtWidgets.QWidget()
        self.CPU_WIDGET_CONT = QtWidgets.QWidget(self.tab_2)
        self.GPU_WIDGET_CONT = QtWidgets.QWidget(self.tab_2)
        self.gpu_temp_check = QtWidgets.QCheckBox(self.tab_2)
        self.gpu_fan_check = QtWidgets.QCheckBox(self.tab_2)
        self.gpu_memory_check = QtWidgets.QCheckBox(self.tab_2)
        self.cpu_temp_check = QtWidgets.QCheckBox(self.tab_2)
        self.cpu_load_check = QtWidgets.QCheckBox(self.tab_2)
        self.LABEL_INFO = QtWidgets.QLabel(self.tab_2)
        self.label_time = QtWidgets.QLabel(self.tab_2)
        self.label_data_amount = QtWidgets.QLabel(self.tab_2)
        self.LABEL_GPU = QtWidgets.QLabel(self.tab_2)
        self.LABEL_CPU = QtWidgets.QLabel(self.tab_2)
        self.line = QtWidgets.QFrame(self.tab_1)

        self.html_title_head = "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">"
        self.html_small_title_head = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"
        self.html_font_end = "</span></p></body></html>"
        self.html_text_head = "<html><head/><body><p><span style=\" font-size:12pt;\">"

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setup_ui()

    def setup_ui(self):
        self.q_tab1.setGeometry(QtCore.QRect(-2, 0, 1032, 772))
        self.q_tab1.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.q_tab1.setObjectName("q_tab1")

        self.tab_1.setObjectName("tab_1")

        self.line.setGeometry(QtCore.QRect(0, 380, 475, 8))
        self.line.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        # Proměnné psané tiskacím by neměly být upravovány

        self.CPU_MAIN_LABEL.setGeometry(QtCore.QRect(35, 15, 165, 45))
        self.CPU_MAIN_LABEL.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CPU_MAIN_LABEL.setTextFormat(QtCore.Qt.AutoText)
        self.CPU_MAIN_LABEL.setObjectName("CPU_MAIN_LABEL")

        self.GPU_MAIN_LABEL.setGeometry(QtCore.QRect(35, 395, 191, 45))
        self.GPU_MAIN_LABEL.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.GPU_MAIN_LABEL.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GPU_MAIN_LABEL.setObjectName("GPU_MAIN_LABEL")

        self.cpu_frequency_label.setGeometry(QtCore.QRect(55, 150, 231, 21))
        self.cpu_frequency_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_frequency_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_frequency_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_frequency_label.setObjectName("cpu_frequency_label")

        self.cpu_cores_label.setGeometry(QtCore.QRect(55, 110, 161, 21))
        self.cpu_cores_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_cores_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_cores_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_cores_label.setObjectName("cpu_cores_label")

        self.cpu_name_label.setGeometry(QtCore.QRect(55, 70, 411, 21))
        self.cpu_name_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_name_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_name_label.setObjectName("cpu_name_label")

        self.cpu_min_temperature_label.setGeometry(QtCore.QRect(55, 230, 231, 21))
        self.cpu_min_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_min_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_min_temperature_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_min_temperature_label.setObjectName("cpu_min_temperature_label")

        self.cpu_max_temperature_label.setGeometry(QtCore.QRect(55, 270, 231, 21))
        self.cpu_max_temperature_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cpu_max_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_max_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_max_temperature_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_max_temperature_label.setObjectName("cpu_max_temperature_label")

        self.cpu_load_label.setGeometry(QtCore.QRect(55, 310, 231, 21))
        self.cpu_load_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_load_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_load_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_load_label.setObjectName("cpu_load_label")

        self.gpu_name_label.setGeometry(QtCore.QRect(55, 455, 231, 21))
        self.gpu_name_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_name_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_name_label.setTextFormat(QtCore.Qt.AutoText)
        self.gpu_name_label.setObjectName("gpu_name_label")

        self.gpu_total_memory_label.setGeometry(QtCore.QRect(55, 495, 231, 21))
        self.gpu_total_memory_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_total_memory_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_total_memory_label.setTextFormat(QtCore.Qt.AutoText)
        self.gpu_total_memory_label.setObjectName("gpu_total_memory_label")

        self.gpu_memory_used_label.setGeometry(QtCore.QRect(55, 655, 301, 21))
        self.gpu_memory_used_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_memory_used_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_memory_used_label.setObjectName("gpu_memory_used_label")

        self.gpu_fan_load_label.setGeometry(QtCore.QRect(55, 695, 311, 21))
        self.gpu_fan_load_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_fan_load_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_fan_load_label.setTextFormat(QtCore.Qt.AutoText)
        self.gpu_fan_load_label.setObjectName("gpu_fan_load_label")

        self.gpu_temperature_label.setGeometry(QtCore.QRect(55, 535, 231, 21))
        self.gpu_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_temperature_label.setTextFormat(QtCore.Qt.AutoText)
        self.gpu_temperature_label.setObjectName("gpu_temperature_label")

        self.gpu_min_temperature_label.setGeometry(QtCore.QRect(55, 575, 291, 21))
        self.gpu_min_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_min_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_min_temperature_label.setTextFormat(QtCore.Qt.AutoText)
        self.gpu_min_temperature_label.setObjectName("gpu_min_temperature_label")

        self.cpu_actual_temperature_label.setGeometry(QtCore.QRect(55, 190, 231, 21))
        self.cpu_actual_temperature_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.cpu_actual_temperature_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cpu_actual_temperature_label.setTextFormat(QtCore.Qt.AutoText)
        self.cpu_actual_temperature_label.setObjectName("cpu_actual_temperature_label")

        self.gpu_max_temp_label.setGeometry(QtCore.QRect(55, 615, 271, 21))
        self.gpu_max_temp_label.setStyleSheet("color: rgb(40, 125, 200);")
        self.gpu_max_temp_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gpu_max_temp_label.setTextFormat(QtCore.Qt.AutoText)
        self.gpu_max_temp_label.setObjectName("gpu_max_temp_label")

        self.line_2.setGeometry(QtCore.QRect(55, 300, 420, 3))
        self.line_2.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3.setGeometry(QtCore.QRect(55, 180, 420, 3))
        self.line_3.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4.setGeometry(QtCore.QRect(55, 140, 420, 3))
        self.line_4.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_5.setGeometry(QtCore.QRect(55, 100, 420, 3))
        self.line_5.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6.setGeometry(QtCore.QRect(55, 220, 420, 3))
        self.line_6.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.line_7.setGeometry(QtCore.QRect(55, 260, 420, 3))
        self.line_7.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.line_8.setGeometry(QtCore.QRect(55, 340, 420, 3))
        self.line_8.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.line_9.setGeometry(QtCore.QRect(55, 485, 420, 3))
        self.line_9.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.line_10.setGeometry(QtCore.QRect(55, 525, 420, 3))
        self.line_10.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

        self.line_11.setGeometry(QtCore.QRect(55, 565, 420, 3))
        self.line_11.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")

        self.line_12.setGeometry(QtCore.QRect(55, 605, 420, 3))
        self.line_12.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")

        self.line_13.setGeometry(QtCore.QRect(55, 645, 420, 3))
        self.line_13.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")

        self.line_14.setGeometry(QtCore.QRect(55, 685, 420, 3))
        self.line_14.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")

        self.line_15.setGeometry(QtCore.QRect(55, 725, 420, 3))
        self.line_15.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")

        self.line_16.setGeometry(QtCore.QRect(0, 440, 475, 3))
        self.line_16.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")

        self.line_17.setGeometry(QtCore.QRect(0, 60, 475, 3))
        self.line_17.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")

        self.line_18.setGeometry(QtCore.QRect(475, 60, 3, 283))
        self.line_18.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")

        self.line_19.setGeometry(QtCore.QRect(475, 440, 3, 288))
        self.line_19.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")

        self.q_tab1.addTab(self.tab_1, "")

        # Odtud začíná 2. sekce s grafy

        self.tab_2.setObjectName("tab_2")

        self.CPU_WIDGET_CONT.setGeometry(QtCore.QRect(440, 40, 561, 301))
        self.CPU_WIDGET_CONT.setObjectName("CPU_WIDGET_CONT")

        self.GPU_WIDGET_CONT.setGeometry(QtCore.QRect(440, 400, 561, 301))
        self.GPU_WIDGET_CONT.setObjectName("GPU_WIDGET_CONT")

        self.gpu_temp_check.setGeometry(QtCore.QRect(30, 680, 81, 21))
        self.gpu_temp_check.setChecked(True)
        self.gpu_temp_check.setTristate(False)
        self.gpu_temp_check.setObjectName("gpu_temp_check")

        self.gpu_fan_check.setGeometry(QtCore.QRect(262, 680, 151, 21))
        self.gpu_fan_check.setChecked(True)
        self.gpu_fan_check.setObjectName("gpu_fan_check")

        self.gpu_memory_check.setGeometry(QtCore.QRect(121, 680, 131, 21))
        self.gpu_memory_check.setChecked(True)
        self.gpu_memory_check.setObjectName("gpu_memory_check")

        self.cpu_temp_check.setGeometry(QtCore.QRect(30, 321, 101, 21))
        self.cpu_temp_check.setChecked(True)
        self.cpu_temp_check.setObjectName("cpu_temp_check")

        self.cpu_load_check.setGeometry(QtCore.QRect(140, 321, 101, 21))
        self.cpu_load_check.setChecked(True)
        self.cpu_load_check.setObjectName("cpu_load_check")

        self.LABEL_INFO.setGeometry(QtCore.QRect(30, 30, 401, 161))
        self.LABEL_INFO.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.LABEL_INFO.setObjectName("LABEL_INFO")

        self.label_time.setGeometry(QtCore.QRect(30, 460, 141, 31))
        self.label_time.setObjectName("label_time")

        self.label_data_amount.setGeometry(QtCore.QRect(30, 491, 141, 31))
        self.label_data_amount.setObjectName("label_data_amount")

        self.LABEL_GPU.setGeometry(QtCore.QRect(30, 640, 321, 31))
        self.LABEL_GPU.setObjectName("LABEL_GPU")

        self.LABEL_CPU.setGeometry(QtCore.QRect(30, 281, 321, 31))
        self.LABEL_CPU.setObjectName("LABEL_CPU")

        self.q_tab1.addTab(self.tab_2, "")
        self.setCentralWidget(self.q_tab1)

        self.style_sheet()

        self.q_tab1.setCurrentIndex(0)

    def style_sheet(self):
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
                                               f"{self.html_text_head}Název procesoru: AMD Athlon II X4 640 Processor"
                                               f"{self.html_font_end}")
                                    )
        self.cpu_min_temperature_label.setText(_translate("main_window",
                                                          f"{self.html_text_head}Nejmenší naměřená teplota °C:"
                                                          f" {self.html_font_end}")
                                               )
        self.cpu_max_temperature_label.setText(_translate("main_window",
                                                          f"{self.html_text_head}Největší naměřená teplota °C:"
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
                                                          f"{self.html_text_head}Nejmenší naměřená teplota °C:"
                                                          f"{self.html_font_end}")
                                               )
        self.cpu_actual_temperature_label.setText(_translate("main_window",
                                                             f"{self.html_text_head}Aktuální teplota °C: "
                                                             f"{self.html_font_end}")
                                                  )
        self.gpu_max_temp_label.setText(_translate("main_window",
                                                   f"{self.html_text_head}Největší naměřená teplota °C:"
                                                   f"{self.html_font_end}")
                                        )

        self.q_tab1.setTabText(self.q_tab1.indexOf(self.tab_1), _translate("main_window", "Sensory"))
        self.gpu_temp_check.setText(_translate("main_window", "Teplota GPU"))
        self.gpu_fan_check.setText(_translate("main_window", "Zatížení větráčku na GPU"))
        self.gpu_memory_check.setText(_translate("main_window", "Vytížení paměti VRAM"))
        self.cpu_temp_check.setText(_translate("main_window", "Teplota CPU"))
        self.cpu_load_check.setText(_translate("main_window", "Zatížení CPU"))

        self.LABEL_INFO.setText(_translate("main_window", f"{self.html_small_title_head}"
                                                          f"Grafy znázorňující informace v závislosti na čase."
                                                          f"{self.html_text_head}"
                                                          f"Pro výběr stačí pomocí zakřížkování vybrat dané"
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

        self.q_tab1.setTabText(self.q_tab1.indexOf(self.tab_2), _translate("main_window", "Grafy"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UIMainWindow()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
