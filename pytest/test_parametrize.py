import pytest
class TestClass:
    @pytest.mark.parametrize('user,pwd',[('a',1),('b',2),('c',3)])
    def test_login(self,user,pwd):
        print("This is parameterization...",user,pwd)