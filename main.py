from service.calculatrice import Calculatrice

if __name__ == '__main__':
    calc = Calculatrice()
    result: int = calc.addition(1, 2)
    print(result)