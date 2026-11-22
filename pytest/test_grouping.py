import pytest

class Test_Grouping:

    @pytest.mark.sanity
    def test_search(self):
        assert False

    @pytest.mark.regression
    def test_login(self):
        assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self):
        assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login2(self):
        assert False

    @pytest.mark.regression
    def test_login3(self):
        assert False

