from calculator import *


class TestCalculadora:

    def test_suma(self):
        calculator = Calculator()
        assert 4 == calculator.sumar(2, 2)

    def test_resta(self):
        calculator = Calculator()
        assert 4 == calculator.restar(4, 2)