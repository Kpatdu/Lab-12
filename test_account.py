import pytest

import account
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account("John")
        self.a2 = Account("Bill")

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == "John"
        assert self.a1.get_balance() == 0

        assert self.a2.get_name() == "Bill"
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.deposit("x") is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.deposit(2) is True
        assert self.a1.get_balance() == pytest.approx(2)

        assert self.a2.deposit(-.012) is False
        assert self.a2.get_balance() == pytest.approx(0)
        assert self.a2.deposit("y") is False
        assert self.a2.get_balance() == pytest.approx(0)
        assert self.a2.deposit(0) is False
        assert self.a2.get_balance() == pytest.approx(0)
        assert self.a2.deposit(1.492) is True
        assert self.a2.get_balance() == pytest.approx(1.492)

    def test_withdraw(self):
        assert self.a1.withdraw(-2) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.withdraw("x") is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == pytest.approx(0)
        self.a1.deposit(2)
        assert self.a1.withdraw(1) is True
        assert self.a1.get_balance() == pytest.approx(1)
        assert self.a1.withdraw(2) is False
        assert self.a1.get_balance() == pytest.approx(1)

        assert self.a2.withdraw(-.12) is False
        assert self.a2.get_balance() == pytest.approx(0)
        assert self.a2.withdraw("y") is False
        assert self.a2.get_balance() == pytest.approx(0)
        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == pytest.approx(0)
        self.a2.deposit(.92)
        assert self.a2.withdraw(0.9) is True
        assert self.a2.get_balance() == pytest.approx(0.02)
        assert self.a2.withdraw(2) is False
        assert self.a2.get_balance() == pytest.approx(0.02)


