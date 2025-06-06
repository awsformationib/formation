


import unittest

from corrections.calc import Calculatrice


class TestCalculatrice(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test."""
        self.calc = Calculatrice()

    def tearDown(self):
        """Nettoyage après chaque test (optionnel ici)."""
        pass

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(self.calc.soustraction(10, 4), 6)

    def test_division_normale(self):
        self.assertEqual(self.calc.division(10, 2), 5)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            self.calc.division(10, 0)

