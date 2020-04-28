from calculator import *


class TestCalculadora:

    def test_suma(self):
        calculator = Calculator()
        assert 4 == calculator.add(2, 2)

    def test_resta(self):
        calculator = Calculator()
        assert 2 == calculator.subtract(4, 2)