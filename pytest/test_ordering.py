import pytest

class Test_Ordering:

    @pytest.mark.third
    def test_m3(self):
        print("This is C...")

    @pytest.mark.second
    def test_m2(self):
        print("This is B...")

    @pytest.mark.fifth
    def test_m5(self):
        print("This is E...")

    @pytest.mark.first
    def test_m1(self):
        print("This is A...")

    @pytest.mark.fourth
    def test_m4(self):
        print("This is D...")



