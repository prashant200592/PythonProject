import pytest

class Test_Class:

    @pytest.mark.dependency()
    def test_openapp(self):
        assert True

    @pytest.mark.dependency(depends=["Test_Class::test_openapp"])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=["Test_Class::test_login"])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=["Test_Class::test_login", "Test_Class::test_search"])
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=["Test_Class::test_login"])
    def test_logout(self):
        assert True

