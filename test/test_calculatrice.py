import unittest
from service.calculatrice import Calculatrice

class TestCalculatrice(unittest.TestCase):
    
    def setUp(self):
        """Initialise une nouvelle instance de la calculatrice pour chaque test."""
        self.calc = Calculatrice()

    def test_addition(self):
        """Teste la méthode d'addition."""
        self.assertEqual(self.calc.addition(1, 2), 3)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(-1, -1), -2)

    def test_soustraction(self):
        """Teste la méthode de soustraction."""
        self.assertEqual(self.calc.soustraction(5, 3), 2)
        self.assertEqual(self.calc.soustraction(-1, 1), -2)
        self.assertEqual(self.calc.soustraction(-1, -1), 0)

