import pytest

@pytest.mark.order(4)
def test_Sample1():
    assert 1+1==2

@pytest.mark.order(1)
@pytest.mark.fail
def test_Sample2():
    assert 1+1==2,"2 needed"

@pytest.mark.order(0)
@pytest.mark.fail
def test_Sample3():
    assert "hi"=="hi"

@pytest.mark.order(3)
def test_Sample4():
    a=10
    b=5
    assert a>b

@pytest.mark.order(2)
def test_Sample5():
    str1="hi"
    str2='hi'

    assert str2.__eq__(str1)

