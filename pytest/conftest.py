import pytest

@pytest.fixture()
def setup():
    print("This is precondition")
    yield
    print("This is conclusion")



