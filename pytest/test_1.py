import pytest

class TestClass:
    @pytest.mark.skip(reason="Testing...")
    def test_m1(self, setup):
        print("This is m1")

    @pytest.mark.sanity
    def test_m2(self, setup):
        print("This is m2")


    def test_m3(self,setup):
        print("This is m3")


