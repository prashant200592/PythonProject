import pytest

class Test_Ordering:

    @pytest.mark.run(order=3)
    def test_m3(self):
        print("This is C...")

    @pytest.mark.run(order=4)
    def test_m4(self):
        print("This is D...")

    @pytest.mark.run(order=5)
    def test_m5(self):
        print("This is E...")

    @pytest.mark.run(order=1)
    def test_m1(self):
        print("This is A...")

    @pytest.mark.run(order=2)
    def test_m2(self):
        print("This is B...")
