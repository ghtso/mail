# zad 8 lista 1 programowanie obiektowe

'''
 Przygotować klasę reprezentującą planetę, atrybuty wydedukować z poniż-
szej tabeli:
(tabela w treści zadania)
'''

class Planeta:

    def __init__(self, nazwa, odleglosc_od_slonca, czy_rzeczywista):
        self.nazwa = nazwa
        self.odleglosc_od_slonca = odleglosc_od_slonca
        self.czy_rzeczywista = czy_rzeczywista

def main():
    print('Teraz jestem w funkcji main()!')
    p = Planeta('Wulkan',0.03,False)
    print(p.nazwa)
    print(p.odleglosc_od_slonca)
    print(p.czy_rzeczywista)
    pass

#
#   run (F5):
#

if __name__ == '__main__':
    main()
