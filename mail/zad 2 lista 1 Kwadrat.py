# zad 2 lista 1
'''
Przygotować klasę opisująca kwadrat
'''

class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok * self.bok


lista = []

for bok in range(5,16,5):
    lista.append(Kwadrat(bok))

for el in lista:
    print('bok = ',el.bok,', pole = ', el.pole())
