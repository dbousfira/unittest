import pytest


def inc(x):
    return x + 1


def f():
    raise SystemExit(1)


# Le retours des fonctions
def test_answer():
    assert inc(3) == 4


# La bonne gestion des erreurs
def test_mytest():
    with pytest.raises(SystemExit):
        f()