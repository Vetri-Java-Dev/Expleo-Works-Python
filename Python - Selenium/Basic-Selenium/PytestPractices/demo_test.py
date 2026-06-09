import pytest

def test_Sample1():
    assert 1+1==2

@pytest.mark.fail
def test_Sample2():
    assert 1+1==3,"2 needed"

@pytest.mark.fail
def test_Sample3():
    assert "hi"=="hii"

def test_Sample4():
    a=10
    b=5
    assert a>b

def test_Sample5():
    str1="hi"
    str2='hi'

    assert str2.__eq__(str1)

