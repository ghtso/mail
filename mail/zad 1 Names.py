# zad 1 lista 1
# SP Programiowaine komputerów ZUT
# programowanie obiektowe
# @ Tomasz Sobolewski
# zajęcia 13-14.02.2016 r.

class Names:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

def test():
    n = Names('Jan','Kowalski')
    n2 = Names('Andrzej','Nowak')
    n3 = Names('Janina','Bogacka')

    for el in [n, n2, n3]:
        print(el.firstName, el.lastName)

def main():
    pass

if __name__ == '__main__':
    test()
    main()
