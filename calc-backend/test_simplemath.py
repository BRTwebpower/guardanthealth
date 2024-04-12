import pytest

from simplemath import app

@pytest.fixture
def client():
    #app.testing = True
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

#@pytest.mark.parametrize("test_input", "expected", [
#    ({'x': 3, 'y': 4}, 
#])

@pytest.mark.parametrize("x", [i for i in range(5)])
@pytest.mark.parametrize("y", [i for i in range(5, 10)])
def test_add(client, x, y):
    rv = client.get(f'/add?x={x}&y={y}')
    rv = rv.data.decode()
    print(f"\n{x}+{y}: {rv}\n")
    assert rv==str(float(x+y))

@pytest.mark.parametrize("x", [i for i in range(5)])
@pytest.mark.parametrize("y", [i for i in range(5, 10)])
def test_sub(client, x, y):
    rv = client.get(f'/sub?x={x}&y={y}')
    rv = rv.data.decode()
    print(f"\n{x}-{y}: {rv}\n")
    assert rv==str(float(x-y))
