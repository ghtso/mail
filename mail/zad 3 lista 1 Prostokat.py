# zad 3 lista 1
'''
Przygotować klasę opisująca prostokąt
'''

class Prostokąt:
    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2

    def pole(self):
        return self.bok1 * self.bok2


def BokiPole(el):
    print(el.bok1, el.bok2, el.pole())



# PROSTOKĄT

print('\n-----prostokąty--------\n')

listaProstokąt = []

for bok in range(5,16,5):
    listaProstokąt.append(Prostokąt(bok, bok * 2))

for el in listaProstokąt:
    print('bok1 = ',el.bok1, 'bok2 = ',el.bok2,', pole = ', el.pole())

print('\n-----prostokąty (funkcja)--------\n')

for el in listaProstokąt:
    BokiPole(el)
