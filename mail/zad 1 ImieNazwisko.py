# zad 1 lista 1
'''
klasa do przechowywania imion i nazwisk
'''


class ImieNazwisko:
    def __init__(self):
##        self.imie = ''
##        self.nazwisko = ''    
        self.lista = []

    def DodajImieNazwisko(self, imie = '', nazwisko = ''):
        self.lista.append(imie + '' + nazwisko)


    def WypiszImionaNazwiska(self):
        for el in lista:
            print(el)

##    def DodajImie(self, imie = ''):
##        lista
##
##    def DodajNazwisko(self, nazwisko = '')


dziennik = ImieNazwisko()

##dziennik.DodajImie('Tomasz')
##dziennik.DodajNazwisko("Sobolewski")

dziennik.DodajImieNazwisko('Tomasz','Sobolewski')
dziennik.DodajImieNazwisko('Tomasz','Sobolewski')
dziennik.DodajImieNazwisko('Tomasz','Sobolewski')

dziennik.WypiszImionaNazwiska()
