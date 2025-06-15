import pytest
from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_positive(self):
        assert self.calc.adding(2, 6) == 8

    def test_adding_negative(self):
        assert self.calc.adding(-2, -3) == -5

    def test_adding_mixed(self):
        assert self.calc.adding(-2, 3) == 1

    def test_subtraction_positive(self):
        assert self.calc.subtraction(10, 4) == 6

    def test_subtraction_negative(self):
        assert self.calc.subtraction(-5, -3) == -2

    def test_subtraction_to_zero(self):
        assert self.calc.subtraction(3, 3) == 0

    def test_multiply_positive(self):
        assert self.calc.multiply(3, 5) == 15

    def test_multiply_by_zero(self):
        assert self.calc.multiply(10, 0) == 0

    def test_multiply_negative(self):
        assert self.calc.multiply(-2, 4) == -8

    def test_division_positive(self):
        assert self.calc.division(20, 4) == 5

    def test_division_negative(self):
        assert self.calc.division(-15, 3) == -5

    def test_division_float(self):
        assert self.calc.division(7, 2) == 3.5

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(10, 0)
