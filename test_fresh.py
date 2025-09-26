import pytest

def test_raises():
    with pytest.raises(Exception) as exc_info:   
        #Вызов функции, которая вызывает Exception
        raise Exception('some info')
    assert exc_info.value.args[0] == 'some info'
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise