from calculator import *


class TestCalculator:

    def test_add(self):
        calculator = Calculator()
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        calculator = Calculator()
        assert 2 == calculator.subtract(4, 2)

