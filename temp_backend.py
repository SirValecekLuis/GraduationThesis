import math
import time
import clr  # Pythonnet modul, zajišťuje propojení s API aplikace
import numpy as np
import csv
import re
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class HWMInit:
    """
    Objekt slouží k základnímu zavedení dll knihovny a aktualizaci dat pomocí metody update()
    """

    def __init__(self):
        clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib')  # Cesta, kde se nachází dll soubor
        from OpenHardwareMonitor.Hardware import Computer  # Z daného místa importuji Computer
        self._computer = Computer()  # Zavedení objektu s daty
        self._computer.CPUEnabled = True  # Chci získávat údaje z processoru, [0] a jejich informace
        self._computer.GPUEnabled = True  # Chci získávat údaje z grafické karty [1] bude označovat grafické senzory
        self._computer.Open()  # Spustím měření
        self.cpu_object = self._computer.Hardware[0]
        self.gpu_object = self._computer.Hardware[1]

    def update(self) -> None:
        """
        Při zavolání updatuje objekt "computer"
        :return: None
        """

        self.cpu_object.Update()
        self.gpu_object.Update()


class CPU:
    """
    CPU objekt slouží k uspořádání dat na jednom místě, objekt bude často volán a tvořen znovu a znovu.
    Při každém volání se změní skoro všechny parametry, objekt by se měl volat při aktualizaci senzorických dat.
    """

    def __init__(self, cpu):
        self.cpu = cpu
        self.name = self.cpu.Name
        self.cores = 0

        if self.name.count("NVIDIA") == 2:
            self.name = self.name.replace("NVIDIA ", "", 1)

        for sensor in cpu.Sensors:
            sensor_name = str(sensor.Identifier)
            if sensor_name == "/amdcpu/0/load/0" or sensor_name == "/intelcpu/0/load/0":
                self.load = round(sensor.Value, 1)  # Vytížení v %
            elif sensor_name == "/amdcpu/0/temperature/0" or sensor_name == "/intelcpu/0/temperature/0":
                self.temperature = round(sensor.Value, 1)  # Teplota v °C
                self.lowest_temp = round(sensor.Min, 1)
                self.highest_temp = round(sensor.Max, 1)
            elif sensor_name == "/amdcpu/0/clock/1" or sensor_name == "/intelcpu/0/clock/1":
                self.frequency = math.ceil(sensor.Value / 100) * 100  # Frekvence v Mhz

            if re.search("Core #[1] - #[0-9]*[0-9]", str(sensor.Name)) is not None:
                self.cores = re.search("- #.*", str(sensor.Name)).group().replace("- #", "")
            elif "/amdcpu/0/load/" in sensor_name or "/intelcpu/0/load/" in sensor_name:
                if int(sensor_name[-1]) > self.cores:
                    self.cores = sensor_name[-1]

    def __repr__(self):
        return f"{self.load},{self.temperature}"


class GPU:
    """
    GPU objekt slouží k uchování senzorických dat z grafické karty, parametry se budou pravidelně měnit.
    Proto bude objekt pravidelně vytvářen znovu a znovu s novými parametry.
    """

    def __init__(self, gpu):
        self.gpu = gpu
        self.name = self.gpu.Name

        for sensor in gpu.Sensors:  # Potřeba otestovat, jestli je to "atigpu" nenalezeno v dokumentaci!
            sensor_name = str(sensor.Identifier)
            if sensor_name == "/nvidiagpu/0/temperature/0" or sensor_name == "/atigpu/0/temperature/0":
                self.temperature = int(sensor.Value)  # Teplota
                self.lowest_temp = int(sensor.Min)
                self.highest_temp = int(sensor.Max)
            elif sensor_name == "/nvidiagpu/0/control/0" or sensor_name == "/atigpu/0/control/0":
                self.fan = int(sensor.Value)  # Větrák vytížení v %
            elif sensor.Name == "GPU Memory Total":
                self.memory_total = int(sensor.Value)  # Celkový počet paměti u GPU
            elif sensor.Name == "GPU Memory":
                self.memory_used = round(sensor.Value, 1)  # Použití paměti v %

    def __repr__(self):
        return f"{self.temperature},{self.fan},{self.memory_used}"


class File:
    """
    Zápis dat jako csv soubor, při vytváření je možné určit jméno souboru.
    Také slouží k vytváření NdArrays z NumPy a jejich aktualizaci.
    """

    def __init__(self, name: str):
        self._last_data = ""
        self.name = name
        self._data_list = []
        self.ndar_list = []
        self.header = []

    def write_data(self, cpu: CPU, gpu: GPU) -> None:
        """
        Funkce zapíše data do souboru.
        :param gpu: Objekt typu GPU
        :param cpu: Objekt typu CPU
        :return: None
        """

        data = repr(cpu) + "," + repr(gpu)  # Složím data dohromady
        self._last_data = data  # Zapíšu je jako poslední balíček dat do objektu
        try:
            with open(self.name, "x") as f:  # Zkusím otevřít soubor, pokud neexistuje, zapíšu header
                f.write("zátěž procesoru %,teplota procesoru °C,teplota grafické karty °C,"
                        "rychlost větráčku na grafice %,vytížení paměti grafické karty %\n"
                        )
                f.write(data + "\n")
        except FileExistsError:  # Pokud soubor existuje, pouze připíšu data
            with open(self.name, "a") as f:
                f.write(data + "\n")

    def _create_data_list(self) -> None:
        """
        Vytvoří 2D seznam se všemi přečtenými údaji ze zadaného souboru.
        Nejdřív by měl být vytvořen data list.
        :return: None
        """

        with open(self.name, "r") as f:
            csv_data = csv.reader(f)
            self.header = next(csv_data)
            for row in csv_data:
                self._data_list.append(row)

    def _create_ndar_list(self) -> None:
        """
        Uloží do listu np.array kde každý array představuje jednu sadu informací s tím že 1. informace arraye je header
        Nejdřív musí být vytvořen data list, aby mohl být vytvořen ndar list.
        :return: None
        """

        for i in range(len(self.header)):
            temp_list = []
            for row in self._data_list:
                temp_list.append(float(row[i]))
            self.ndar_list.append(np.array(temp_list))

    def update_ndar_list(self) -> None:
        """
        Funkce slouží k rozšíření každého balíčku ndarray dat aby se aktualizovala data.
        Pokud jde o 1. spuštění souboru a nejsou zapsaná data v paměti, soubor je načte a uloží.
        :return: None
        """

        if not self._data_list and not self.ndar_list:  # Pokud neexistuje data_list, vytvořím ho
            self._create_data_list()
            self._create_ndar_list()
        else:
            for i in range(len(self.header)):
                data_to_update = self._last_data.split(",")[i]
                self.ndar_list[i] = np.concatenate((self.ndar_list[i], [float(data_to_update)]))


class Graph(FigureCanvasQTAgg):
    def __init__(self, data: np.ndarray, header: list):
        # https://matplotlib.org/3.5.1/gallery/user_interfaces/embedding_in_qt_sgskip.html
        figure = Figure()  # Vytvořím základní místo pro graf
        super().__init__(figure)  # Dědím ze třídy FigureCanvas pro svoji proměnnou figure
        self.sub = figure.add_subplot()  # Vytvořím jednotlivé políčko pro graf

        self.header = header  # Všechna záhlaví pro daný graf

        index = 0  # Potřebuji dočasnou proměnou na to, abych určil jaké záhlaví použít
        if len(data) == 2:
            index = 1
            self.data_y = data[index]  # 2 sloupce, 2. sloupec je teplota
            self.sub.set_title("Procesor")
        else:
            self.sub.set_title("Grafická karta")
            self.data_y = data[index]  # 3 sloupce, 1. sloupec je teplota

        self.data_x = np.linspace(0, len(data[0]), len(data[0]))  # Vytvořím si pole odpovídající velikosti dat
        self.graph, = self.sub.plot(self.data_x, self.data_y,
                                    "-b", label=header[index])  # Vykreslím teplotu vzhledem k času
        self.legend = self.sub.legend(loc='upper center', fancybox=True, bbox_to_anchor=(0.5, 1.05), shadow=True)
        # Nastavení legendy
        self.sub.set_xlabel("t (čas)")
        self.sub.set_ylabel(header[index])
        self.sub.tick_params(bottom=False)  # Oddělá prostřední čárky pro časovou osu
        self.sub.set_xticks([])  # Oddělá čísla pro časovou osu

    def update_data(self, data: np.ndarray, index: int):
        """Funkce slouží k novému nahrání dat z předešlé doby"""

        self.data_x = np.linspace(0, len(data[0]), len(data[0]))  # Vypíšu rozmezí časové od 0 do počet dat(počet sec)
        self.graph.set_data(self.data_x, data[index])  # Nastavím nové informace
        self.sub.set_xlim(0, len(data[0]))  # Data[0] znamená jen kvůli počtu sekund (počet měření = počet s)
        self.sub.set_ylim(min(data[index]) - 0.5, max(data[index]) + 1.5)  # Nastavím nový rozsah sloupce
        self.sub.set_ylabel(self.header[index])  # Přejmenuji Y osu
        self.legend.get_texts()[0].set_text(self.header[index])  # Přejmenuji legendu grafu
        self.graph.figure.canvas.draw()  # Zobrazí aktuální graf


# Testovací část, spouští se pokud se spouští přímo zdrojový kód temp_backend.py
def test(cpu_object, gpu_object) -> print:
    """
    Funkce slouží k testování a základnímu ladění programu.
    :param cpu_object: Objekt typu CPU
    :param gpu_object: Objekt typu GPU
    :return: Vytiskne veškerá senzorická data s jejími názvy a dalšími informacemi, slouží pro debugging.
    """

    for i in cpu_object.Sensors:
        try:
            print(i.Value, i.Name, i.Identifier, i.SensorType)
        except:
            print("except")
            print(i.Value, i.Name, i.Identifier, i)
    print(60 * "#")
    for i in gpu_object.Sensors:
        try:
            print(i.Value, i.Name, i.Identifier, i.SensorType)
        except:
            print("except")
            print(i.Value, i.Name, i.Identifier, i)
    time.sleep(5)


def main():
    """
    Funkce slouží k zavolání všech potřebných věcí a chodu kódu.
    :return: None
    """

    computer_object = HWMInit()  # Obsahuje objekty s kterými mohu pracovat(co senzor to objekt)
    file = File("data.csv")  # Název souboru
    inp = input("Zadej režim: ") == "normal"
    while True:
        if inp:
            computer_object.update()
            cpu = CPU(computer_object.cpu_object)
            gpu = GPU(computer_object.gpu_object)
            file.write_data(cpu, gpu)
            file.update_ndar_list()
            time.sleep(2)
        else:
            computer_object.update()
            cpu = computer_object.cpu_object
            gpu = computer_object.gpu_object
            test(cpu, gpu)


if __name__ == "__main__":
    main()
