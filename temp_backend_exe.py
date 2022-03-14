import clr  # Pythonnet modul, zajišťuje propojení s API aplikace
import matplotlib


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
        try:
            self.gpu_object = self._computer.Hardware[1]
        except IndexError:
            self.gpu_object = None

    def update(self) -> None:
        """
        Při zavolání updatuje objekt "computer"
        :return: None
        """

        self.cpu_object.Update()
        if self.gpu_object:
            self.gpu_object.Update()


# Testovací část, spouští se pokud se spouští přímo zdrojový kód temp_backend.py
def test(cpu_object, gpu_object) -> print:
    """
    Funkce slouží k testování a základnímu ladění programu.
    :return: Vytiskne veškerá senzorická data s jejími názvy a dalšími informacemi, slouží pro debugging.
    """

    for i in cpu_object.Sensors:
        with open("info.txt", "a") as f:
            f.write(str(i.Value) + "   " + str(i.Name) + "   " + str(i.Identifier) + "\n")
    else:
        with open("info.txt", "a") as f:
            f.write(100 * "    " + "\n")

    for i in gpu_object.Sensors:
        with open("info.txt", "a") as f:
            f.write(str(i.Value) + "   " + str(i.Name) + "   " + str(i.Identifier) + "\n")
    else:
        with open("info.txt", "a") as f:
            f.write(100 * "    " + "\n")

    for i in dir(gpu_object):
        with open("info.txt", "a") as f:
            f.write(str(getattr(gpu_object, i)) + "   " + i + "\n")


computer_object = HWMInit()  # Obsahuje objekty s kterými mohu pracovat(co senzor to objekt)
with open("info.txt", "w") as f:
    f.write("INFORMACE\n" + 100 * "#" + "\n")
computer_object.update()
cpu = computer_object.cpu_object
gpu = computer_object.gpu_object
test(cpu, gpu)
