class Calculatrice:
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            raise Exception('Division par zéro impossible')
        return a / b
