import pytest

class Test_Flaky:

    @pytest.mark.flaky
    def test_flaky(self):
        assert False

    def test_m2(self):
        assert True

