

class Worker:

    def __init__(self, wage=0, bonus=0):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.position = 'slave'
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname} {self.position}')

    def get_total_income(self):
        print(self._income['wage']+self._income['bonus'])

pos = Position(10000, 3000)
pos.get_full_name()
pos.get_total_income()

