class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f'сумма = {self.__cpu + self.__memory} и разность {self.__memory - self.__cpu}'

    def __str__(self):
        return f'компьютер с cpu: {self.__cpu} и memory: {self.__memory}'

    def __gt__(self, other):
        return self.__cpu > other.cpu
    def __lt__(self, other):
        return self.__cpu < other.cpu
    def __eq__(self, other):
        return self.__cpu == other.cpu
    def __ne__(self, other):
        return self.__cpu != other.cpu
    def __le__(self, other):
        return self.__cpu <= other.cpu
    def __ge__(self, other):
        return self.__cpu >= other.cpu

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f'Звонок на номер {call_to_number} по сим карте 1 - О!'
        elif sim_card_number == 2:
            return f'Звонок на номер {call_to_number} по сим карте 2 - Beeline'

    def __str__(self):
        return f'телефон со списком номеров: {self.__sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        return f'построен маршрут от вашей точки до {location}'

    def __str__(self):
        return f'смартфон с cpu: {self.cpu} memory: {self.memory} и списком номеров: {self.sim_cards_list}'


computer = Computer(16, 128)
phone = Phone(['0700564323', '0556345263', '0700564473', '0556285263'])
smartphone1 = SmartPhone(8,64,['0707546253', '0502563522'])
smartphone2 = SmartPhone(20,256, ['0702354747','0506728292'])

print(computer)
print(computer.make_computations())
print(phone)
print(phone.call(1, '0700564323'))
print(smartphone1)
print(smartphone1.use_gps('Цум'))
print(smartphone2)
print(smartphone2.use_gps('Кокжар'))
print(f'компьютер мощнее чем смартфон1: {computer.cpu > smartphone1.cpu}')
print(f'компьютер слабее чем смартфон2: {computer.cpu < smartphone2.cpu}')
print(f'смартфон2 мощнее или равен смартфону1: {smartphone2.cpu >= smartphone1.cpu}')
print(f'компьютер слабее или равен смартфону2: {computer.cpu <= smartphone2.cpu}')
print(f'компьютер не равен смартфону1: {computer.cpu != smartphone1.cpu}')
print(f'компьютер равен смартфону2: {computer.cpu == smartphone2.cpu}')
