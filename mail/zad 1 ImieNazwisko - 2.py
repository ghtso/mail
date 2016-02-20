# zad 1 lista 1
'''
klasa do przechowywania imion i nazwisk
'''


class ImieNazwisko:
    def __init__(self, imie = '', nazwisko = ''):
        self.imie = imie
        self.nazwisko = nazwisko    

    def WypiszImieNazwisko(self):
        print('Imię = ',self.imie, 'Nazwisko = ', self.nazwisko)



def WypiszImNz(el):
    print(el.imie, el.nazwisko)
    return None


n1 = ImieNazwisko('A','B')
n2 = ImieNazwisko('C','D')
n3 = ImieNazwisko('E','F')


##print('1. ',  n1.WypiszImieNazwisko())

print('1. ', end='')
n1.WypiszImieNazwisko()

print('2. ',n2.imie, n2.nazwisko)

print('3. ', end='')
WypiszImNz(n3)
