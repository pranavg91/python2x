import pytest
@pytest.fixture

def sample_data():
    data =[1,2,3,4,5]
    return data
@pytest.fixture()
def sample_data2():
    return True

def test_sample1(sample_data,sample_data2):
    assert sample_data2 == True
    assert len(sample_data) == 5
def test2(sample_data):
    assert 3 in sample_data

def test3(sample_data):
    assert 5 in sample_data