# zad 2 lista 1
# SP Programiowaine komputerów ZUT
# programowanie obiektowe
# @ Tomasz Sobolewski
# zajęcia 13-14.02.2016 r.

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def test():
    s = Square(10)
    s2 = Square(30)
    s3 = Square(15)

    for el in [s, s2, s3]:
        print(el.side,' ', el.area())

def main():
    pass

if __name__ == '__main__':
    test()
    main()
