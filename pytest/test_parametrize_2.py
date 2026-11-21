# @pytest.mark.parametrize(",",[(),(),()])
# pytest-rerunfailures >> --rerun 2

import pytest

class Test_Parametrize:
    @pytest.mark.parametrize("a,b",[(1,3),(3,3),(3,5),(5,5),(5,7)])
    def test_parametrize(self,a,b):
        if a == b:
            assert True
        else:
            assert False
