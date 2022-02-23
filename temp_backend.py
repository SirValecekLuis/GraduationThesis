import math
import time
import clr  # Pythonnet modul, zajišťuje propojení s API aplikace
import numpy as np
import csv


class HWMInit:
    """
    Objekt slouží k základnímu zavedení dll knihovny a aktualizaci dat pomocí metody update()
    """

    def __init__(self):
        clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib')  # Cesta, kde se nachází dll soubor
        from OpenHardwareMonitor.Hardware import Computer  # Z daného místa importuji Computer
        self.computer = Computer()  # Zavedení objektu s daty
        self.computer.CPUEnabled = True  # Chci získávat údaje z processoru, [0] a jejich informace
        self.computer.GPUEnabled = True  # Chci získávat údaje z grafické karty [1] bude označovat grafické senzory
        self.computer.Open()  # Spustím měření

    def update(self) -> None:
        """
        Při zavolání updatuje objekt "computer"
        :return: None
        """

        self.computer.Hardware[0].Update()
        self.computer.Hardware[1].Update()


class CPU:
    """
    CPU objekt slouží k uspořádání dat na jednom místě, objekt bude často volán a tvořen znovu a znovu.
    Při každém volání se změní skoro všechny parametry, objekt by se měl volat při aktualizaci senzorických dat.
    """

    def __init__(self, cpu):
        self.cpu = cpu
        self.name = self.cpu.Name

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
        self._header = []

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
            self._header = next(csv_data)
            for row in csv_data:
                self._data_list.append(row)

    def _create_ndar_list(self) -> None:
        """
        Uloží do listu np.array kde každý array představuje jednu sadu informací s tím že 1. informace arraye je header
        Nejdřív musí být vytvořen data list, aby mohl být vytvořen ndar list.
        :return: None
        """

        for i in range(len(self._header)):
            temp_list = [self._header[i]]
            for row in self._data_list:
                temp_list.append(row[i])
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
            for i in range(len(self._header)):
                data_to_update = self._last_data.split(",")[i]
                self.ndar_list[i] = np.concatenate((self.ndar_list[i], [data_to_update]))


# Testovací část, spouští se pokud se spouští přímo zdrojový kód temp_backend.py

def test(cpu_object: CPU, gpu_object: GPU) -> print:
    """
    Funkce slouží k testování a základnímu ladění programu.
    :param cpu_object: Objekt typu CPU
    :param gpu_object: Objekt typu GPU
    :return: Vytiskne veškerá senzorická data s jejími názvy a dalšími informacemi, slouží pro debugging.
    """

    for i in cpu_object.cpu.Sensors:
        try:
            print(i.Value, i.Name, i.Identifier, i.SensorType)
        except:
            print("except")
            print(i.Value, i.Name, i.Identifier, i)
    print(60 * "#")
    for i in gpu_object.gpu.Sensors:
        try:
            print(i.Value, i.Name, i.Identifier, i.SensorType)
        except:
            print("except")
            print(i.Value, i.Name, i.Identifier, i)
    print(cpu_object.lowest_temp, cpu_object.highest_temp)
    print(gpu_object.lowest_temp, gpu_object.highest_temp)
    time.sleep(2)


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
            cpu_object = computer_object.computer.Hardware[0]
            gpu_object = computer_object.computer.Hardware[1]
            cpu = CPU(cpu_object)
            gpu = GPU(gpu_object)
            computer_object.update()
            file.write_data(cpu, gpu)
            file.update_ndar_list()
            print(file.ndar_list)
            print(cpu.lowest_temp, cpu.highest_temp)
            print(gpu.lowest_temp, gpu.lowest_temp)
            time.sleep(2)
        else:
            cpu_object = computer_object.computer.Hardware[0]
            gpu_object = computer_object.computer.Hardware[1]
            cpu = CPU(cpu_object)
            gpu = GPU(gpu_object)
            computer_object.update()
            test(cpu, gpu)


if __name__ == "__main__":
    main()
