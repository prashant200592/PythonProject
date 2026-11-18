import pytest
class TestClass:
    @pytest.mark.dependency()
    def test_m1(self,setup):
        assert False

    @pytest.mark.dependency(depends=["TestClass::test_m1"])
    def test_m2(self,setup):
        assert True

