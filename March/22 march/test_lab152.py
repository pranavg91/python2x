import pytest

def test_sub():
    assert 2-2 == 0

@pytest.mark.smoke
def test_sub1():
    assert 2-2 == 0

@pytest.mark.reg
def test_sub2():
    assert 2-2 == 0